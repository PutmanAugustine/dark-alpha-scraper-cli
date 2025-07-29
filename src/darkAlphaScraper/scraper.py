import typer
from typing_extensions import Annotated
import os
import pandas as pd
from configparser import ConfigParser
import json
from datetime import datetime
from darkAlphaScraper.contact_scraper import scrape_contacts_with_selenium
from darkAlphaScraper.pagination import scrape_all_deals_with_pagination
from darkAlphaScraper.helper import sheet_to_csv_url
from darkAlphaScraper.helper import parse_money
from darkAlphaScraper.config import (GOOGLE_SHEET_EDIT_URL, FIRM_COL, URL_COL, EXCEL_COLUMNS)
from darkAlphaScraper.helper import map_to_excel
from darkAlphaScraper.save_deals import save_file

config = ConfigParser()
config.read('config.ini')
if not config.has_section('main'):
    config.add_section('main')


def scraper(
  website: Annotated[str, typer.Argument(help="The website to be scraped (if left blank, enters into interactive mode)")] = "",
  output: Annotated[str, typer.Option(help="The file to output the scraped data into (leave blank if entering interactive mode)")] = "",
  geminiToken: Annotated[str, typer.Option(help="Your Gemini API token")] = "",
):
  if not geminiToken == "":
    config.set('main', 'geminiToken', geminiToken)

    with open('config.ini', 'w') as f:
      config.write(f)

    return
  dynamic = website == ""
  if not dynamic:
    scrape(website, output)
  else:
    callToDynamicScraper()

def callToDynamicScraper():
  looping = True
  while looping:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Type 'h' for help.")
    command = input("Enter a command:")
    match command:
      case "h":
        printHelp()
      case "s":
        scrapeQuestions()
      case "q":
        looping = False
      case _:
        print("Invalid command")

def printHelp():
  input("Type 's' to scrape a website.\nType 'q' to quit.\nType 'h' to see this menu again.\nPress 'enter' to continue")

def scrapeQuestions():
  website = input("Enter the URL of the website you'd like to scrape: ")
  outputFile = input("Enter the file you would like to print the scrapped data into: ")
  firmName = input("Enter the name of the firm you are scraping: ")
  scrape(firmName, website, outputFile)

def scrape(firm_name, url, outputFile):
  existing_data = []
  # Track (firm, URL, dealCaption) triplets to avoid duplicates
  existing_keys = {
    (
      d.get("brokerage", "").strip(),
      d.get("sourceWebsite", "").strip(),
      d.get("dealCaption", "").strip()
    )
    for d in existing_data
  }

  df = pd.read_csv(sheet_to_csv_url(GOOGLE_SHEET_EDIT_URL))
  all_data = existing_data.copy()
  deal_caption = ""
  # Skip if this firm + URL + dealCaption combo was already scraped
  if (firm_name, url, deal_caption) in existing_keys:
    print(f"⏩ Skipping already scraped: {firm_name} — {url} — {deal_caption}")
    return
  print(f"🔍 Scraping {firm_name} — {url} — {deal_caption}")
  try:
    deals = scrape_all_deals_with_pagination(url)
    contact_info = scrape_contacts_with_selenium(url, firm_name)
    if not deals:
      print(f"No deals found for {firm_name}")
    for deal in deals:
      deal_caption = deal.get("dealCaption") or deal.get("title", "Not Found")
      key = (firm_name, deal_caption)
      if key in existing_keys:
        continue
      # Clean and parse numbers using parse_money
      revenue = parse_money(deal.get("revenue"))
      ebitda = parse_money(deal.get("ebitda"))
      asking_price = parse_money(deal.get("askingPrice"))
      ebitdaMargin = round((ebitda / revenue) * 100, 2) if ebitda and revenue else None
      gross_revenue = revenue  # assuming same as revenue for now
      # Prepare and append data to Excel & JSON
      data = {
        "id": "",
        "brokerage": firm_name,
        "firstName": contact_info.get("First Name") if contact_info else None,
        "lastName": contact_info.get("Last Name") if contact_info else None,
        "email": contact_info.get("Email") if contact_info else None,
        "linkedinUrl": contact_info.get("LinkedIn URL") if contact_info else None,
        "workPhone": contact_info.get("Work Phone") if contact_info else None,
        "dealCaption": deal.get("title") or deal_caption,
        "revenue": revenue,
        "ebitda": ebitda,
        "title": deal.get("title") or None,
        "grossRevenue": gross_revenue,
        "askingPrice": asking_price,
        "ebitdaMargin": ebitdaMargin,
        "industry": deal.get("industry") or "Not Found",
        "dealType": "MANUAL",
        "sourceWebsite": deal.get("sourceWebsite"),
        "companyLocation": contact_info.get("Company Location") if contact_info else None,
        "createdAt": datetime.utcnow().isoformat() + "Z",
        "updatedAt": datetime.utcnow().isoformat() + "Z",
        "bitrixId": None,
        "bitrixCreatedAt": None,
        "SIM": [],
        "AiScreening": []
      }
      all_data.append(data)
      existing_keys.add(key)
      save_file(all_data, outputFile, EXCEL_COLUMNS, map_to_excel)
      print("Deals saved to excel sheet")
  except Exception as e:
    print(f"Error scraping {firm_name}: {e}")
    # 🔥 Save what has been collected so far before crashing
    save_file(all_data, outputFile, EXCEL_COLUMNS, map_to_excel)
    print(f"Emergency save done after crash on {firm_name}")
