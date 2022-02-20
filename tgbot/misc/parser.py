import requests
from bs4 import BeautifulSoup


#parse the price and product name from the citilink website
async def citilink(link):
    responce = requests.get(link)
    soup = BeautifulSoup(responce.text, 'lxml')
    block = soup.find('div', class_ = "ProductCardLayout__product-description")

    price = block.find('span', class_ = "ProductHeader__price-default_current-price js--ProductHeader__price-default_current-price")
    name_product = block.find('h1', class_ = "Heading Heading_level_1 ProductHeader__title")

    if price is None:
        price = block.find('h2', class_ = "ProductHeader__not-available-header")

    return name_product.get_text(strip = True), price.get_text(strip = True)