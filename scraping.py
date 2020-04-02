from bs4 import BeautifulSoup
import requests
import csv


url = "https://summerofcode.withgoogle.com/archive/2019/projects/"
r = requests.get(url)
page_source = r.text
soup = BeautifulSoup(page_source, 'html.parser')

collist = []
for card in soup.find_all("md-card"):
    name = card.div.contents[1].a.string
    project = card.div.contents[3].string
    organisation = card.div.contents[5].string.replace("Organization: ", "")
    rowlist = []
    rowlist.append(name)
    rowlist.append(organisation)
    rowlist.append(project)
    collist.append(rowlist)

myFile = open('output.csv', 'w')
with myFile:
   writer = csv.writer(myFile)
   writer.writerows(collist)