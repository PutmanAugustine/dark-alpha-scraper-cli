import typer
from typing_extensions import Annotated
import os

def scraper(
  website: Annotated[str, typer.Argument(help="The website to be scraped (if left blank, enters into interactive mode)")] = "",
  output: Annotated[str, typer.Option(help="The file to output the scraped data into (leave blank if entering dynamic mode)")] = "",
):
  dynamic = website == ""
  if not dynamic:
    callToWebscraper(website, output)
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
        scrape()
      case "q":
        looping = False
      case _:
        print("Invalid command")

def printHelp():
  input("Type 's' to scrape a website.\nType 'q' to quit.\nType 'h' to see this menu again.\nPress 'enter' to continue")

def scrape():
  website = input("Enter the URL of the website you'd like to scrape.")
  print("Scraping it")
  outputFile = input("Enter the file you would like to print the scrapped data into.")
  print("Putting it somewhere")

def callToWebscraper(website, output):
  if output == "":
    print("This is where we call the scraper and have it scrape " + website + ", then store the results in " + website + ".xcls")
  else:
    print("This is where we call the scraper and have it scrape " + website +", then store the results in " + output)
