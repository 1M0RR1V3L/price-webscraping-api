from fastapi import FastAPI, Query
from app.scraping import scrape_product

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Price Scraper API is running"}

@app.get("/scrape")
async def scrape(url: str = Query(..., description="Product page URL")):
    """Endpoint for web scraping in a URL"""
    data = await scrape_product(url)
    return data
