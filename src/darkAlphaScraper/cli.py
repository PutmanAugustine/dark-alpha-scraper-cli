import typer

from darkAlphaScraper.scraper import scraper

app = typer.Typer()
app.command()(scraper)

if __name__ == "__main__":
	app()
