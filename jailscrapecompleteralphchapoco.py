#The following two lines of code are meant to import libraries, packages meant to allow the user to perform a series of functions that could not be done without it. 

import urllib2, csv
# The line of code about is a library that allows the user to convert files to comma separated values files. 
from bs4 import BeautifulSoup
#This line of code is meant to extract a class designated as "bs4" from a library called "BeautifulSoup".

#The following lines of code appear to designate variables for later use.
outfile = open('jaildata.csv', 'w')
#Outfile is a variable meant with a method designated as "open". That is probably meant to open the file called jaildata.csv and w, both of which are inside the parentheses.  
writer = csv.writer(outfile)
#writer is a variable whose function is to print out in a csv file of whatever is in the outfile, which in this case is the jaildata.csv.
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#This variable is meant to open the website of interest.
html = urllib2.urlopen(url).read()
#This variable is meant to open and use the package the urllib2 package that was imported, which will open the url and read it. 
soup = BeautifulSoup(html, "html.parser")
#This variable is meant to use the package "BeautifulSoup" and use that library to perform a task using the html variable which is meant to perform another task related the website of interest. 
tbody = soup.find('tbody', {'class': 'stripe'})
#This varibale is meant to find a table element within the website of interest. I have not idea what the "class" and "stripe" means. 
rows = tbody.find_all('tr')
#This variable is meant to find all of the table rows within the table element of the website.
#The next series of codes is meant to perform a loop function.
for row in rows:
#This line is a loop that is meant to go over each row.
    cells = row.find_all('td')
#This statement imples that in each rowm find all of the table elements within each row.
    data = []
#This is a variable that is an empty list.
    for cell in cells:
        data.append(cell.text.encode('utf-8'))
#This is another loop that is meant to find each cell within a table in a row and then convert it to a text, and then place it in 
    writer.writerow(data)
#I believe the function creates strings out of the data when it is extracted from the website. 