
from bs4 import BeautifulSoup
import requests
###########################################################
##  this script prints the top 250 rated                 ##
##  movies from imdb website.                            ##
##  Any website can be scrapped replacing the url        ##
##  and changing the loop for finding rows and columns.  ##
###########################################################
url = "www.imdb.com/chart/top"
r  = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data)

'''headings = []           ###extracting heading
tableheading = soup.find('thead')
heading = tableheading.findAll('tr')
for h in heading:
    headings.append(h.text.strip())
    print (headings)
''' 
dataset = []
table = soup.find('tbody', attrs={'class': 'lister-list'})
rows = table.findAll('tr')
for row in rows:
    column = row.findAll('td')
    column = [element.text.strip() for element in column]
    dataset.append([element for element in column if element])
for i in dataset:
    print (" ".join(i[0].split())+" "+ i[1]) 
