# Price Web Scraping API

A web scraping API designed to fetch product information from online stores.

## Features

- Extracts product names and prices from Mercado Livre.
- Built using FastAPI for a lightweight and efficient API.
- Uses `requests` and `BeautifulSoup` for web scraping.

## Installation

### 1. Clone the repository

```sh
git clone https://github.com/1M0RR1V3L/price-webscraping-api.git
cd price-webscraping-api
```

### 2. Create a virtual environment and activate it

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### Running the API

Start the FastAPI server:

```sh
uvicorn main:app --reload
```
Access the interactive API documentation at:

- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

### Usage

## Scraping a Product

Make a GET request to scrape a product page:

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/scrape?url=<PRODUCT_URL>' \
  -H 'accept: application/json'
```
Or test it via the API docs:
http://127.0.0.1:8000/docs#/default/scrape_scrape_get

### Example Response

```sh
{
  "product_name": "Sample Product",
  "price": 39.0
}
```

### Next Steps

- Implement database storage for scraped data.
- Add support for additional e-commerce platforms.
- Improve error handling and logging.
- Add tracker.
- Add history.
- Telegram notification.

### License

This project is licensed under the MIT License.

```sh

Esse código está pronto para ser copiado e salvo diretamente no arquivo `README.md`. Me avise se precisar de ajustes! 🚀

```


 

