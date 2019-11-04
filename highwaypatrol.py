######## Step One: Getting the libraries########

import requests
from bs4 import BeautifulSoup

########Step Two: Getting the libraries########
url = "https://www.mshp.dps.missouri.gov/HP68/SearchAction"

########Step Three: Requesting information########
r = requests.post(url, data={"searchDate": "10/31/2017"})
html = r.content
########Step Four: Parsing with Beautiful Soup########
soup = BeautifulSoup(html, "html.parser")
########Step Four: Digging into the website########
main_table = soup.find("table", {"class" : "accidentOutput"})
rows = main_table.find_all("tr")

for row in rows:
	table_elements = row.find_all("td")
	print(table_elements)




