import requests, mechanize
from bs4 import BeautifulSoup

url = 'https://www.mshp.dps.missouri.gov/HP68/SearchAction'

br = mechanize.Browser()
br.open(url)
html = br.response().read