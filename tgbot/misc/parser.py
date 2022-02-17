import asyncio
import requests
from bs4 import BeautifulSoup

async def citilink(link):
    responce = requests.get(link)
    soup = BeautifulSoup(responce.text, 'lxml')
    block = soup.find('div', class_ = "ProductCardLayout__product-description")
    price = block.find('span', class_ = "ProductHeader__price-default_current-price js--ProductHeader__price-default_current-price")

    name_product = block.find('h1', class_ = "Heading Heading_level_1 ProductHeader__title")

    return [name_product.get_text(strip = True), price.get_text(strip = True)]    
    