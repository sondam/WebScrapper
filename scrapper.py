###########################################################
##  this script prints the top 250 rated                 ##
##  movies from imdb website, called web scrapper.       ##
##  Any website can be scrapped replacing the url        ##
##  and changing the loop for finding rows and columns.  ##
###########################################################

import requests
from BeautifulSoup import BeautifulSoup

##    specify url to access ##############
url = 'http://www.imdb.com/chart/top'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html) 

##  scanning table body with class lister-list ##############
table = soup.find('tbody', attrs={'class': 'lister-list'})

for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;','')
        print text.replace('12345678910NOT YET RELEASEDSeen',' ')
       
