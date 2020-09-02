from bs4 import BeautifulSoup
import urllib.request
from time import sleep
from datetime import datetime

req= urllib.request.urlopen('http://books.toscrape.com/')

page = req.read()
scraping= BeautifulSoup(page, features='html.parser')
products= scraping.findAll("article", attrs={"class":"product_pod"})

print(products)
