import typer
from typing_extensions import Annotated

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
  pass

def callToWebscraper(website, output):
  if output == "":
    print("This is where we call the scraper and have it scrape " + website + ", then store the results in " + website + ".xcls")
  else:
    print("This is where we call the scraper and have it scrape " + website +", then store the results in " + output)
