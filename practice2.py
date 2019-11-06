import csv
import requests, mechanize
from bs4 import BeautifulSoup

csvfile = open("patrol.csv", "a")
patrol_writer = csv.writer(csvfile)

url = "https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchFirst=&searchLast=&searchCounty=&searchTroop=&searchLocation=&searchCity=&searchDate=10%2F31%2F2017&searchInjury="

br = mechanize.Browser()
br.open(url)
html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

main_table = soup.find("table", {"class": "accidentOutput"})

row_list = main_table.find_all("tr")

for row in row_list:
	table_cells = row.find_all("td")

	output = []
	
	for cell in table_cells:
		output.append(cell.text)
	patrol_writer.writerow(output)






