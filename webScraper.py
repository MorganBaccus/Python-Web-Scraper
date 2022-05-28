from hashlib import new
import requests
from bs4 import BeautifulSoup as bs
import csv

# Webpage to scrape data from
URL = 'https://catalog.wsu.edu/General/Academics/Courses/CPT_S'

# Making a GET request
r = requests.get(URL)

# Parsing the HTML
soup = bs(r.text, 'lxml')

# Finding all instances of course header and course data
titles = soup.find_all('span', {'class': 'course_header'})
infos = soup.find_all('span', {'class': 'course_data'})

# Creating the empty lists to store the dictionaries in
titlesList = []
infosList = []

# Pairing the column name with the text to be stored
for title in titles:
    d1 = {}
    d1['Course Name'] = title.text
    titlesList.append(d1)
for info in infos:
    d2 = {}
    d2['Course Info'] = info.text
    infosList.append(d2)

# Combining the dictionaries so that they can be printed in the same row
i = 0
for title in range(0,len(titlesList)-1):
    titlesList[i].update(infosList[i])
    i+=1

# Writing to the CSV files
filename = 'cptsCourses.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Course Name','Course Info'])
    w.writeheader()
     
    w.writerows(titlesList)
