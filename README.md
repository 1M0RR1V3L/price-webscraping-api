Price Web Scraping API

Repository

GitHub Repository

Project Overview

This project is an API for web scraping product prices from e-commerce websites. The API is built using FastAPI and Python, enabling users to retrieve product details, including prices, via HTTP requests.

Features Implemented

FastAPI setup and configuration

Basic web scraping functionality

Extracting product names and prices from Mercado Livre

Setup Instructions

Requirements

Python 3.10+

FastAPI

BeautifulSoup4

Requests

Uvicorn

Installation

Clone the repository:

git clone https://github.com/1M0RR1V3L/price-webscraping-api.git
cd price-webscraping-api

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Running the API

Start the FastAPI server:

uvicorn main:app --reload

The API documentation will be available at:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

Testing the Scraper

Send a GET request to the scraping endpoint using Swagger UI or via cURL:

curl -X 'GET' 'http://127.0.0.1:8000/scrape?url=<product_url>' -H 'accept: application/json'

Alternatively, test via the interactive documentation at:
http://127.0.0.1:8000/docs#/default/scrape_scrape_get

Next Steps

Improve error handling for different e-commerce structures

Implement scheduled scraping using Celery

Add support for more e-commerce platforms

Store scraped data in PostgreSQL

Add tracker for products

Add user

Add history

