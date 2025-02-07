import httpx
from bs4 import BeautifulSoup

async def scrape_product(url: str):
    """Realiza scraping para obter nome e preço do produto do Mercado Livre"""
    headers = {"User-Agent": "Mozilla/5.0"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch the page", "status": response.status_code}

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1")

    price_meta = soup.find("meta", {"itemprop": "price"})
    price = price_meta["content"] if price_meta else "Not found"

    return {
        "title": title.text.strip() if title else "Not found",
        "price": f"R$ {price}" if price != "Not found" else price,
    }
