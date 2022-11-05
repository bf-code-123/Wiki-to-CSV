import requests #to manipulate web page
from bs4 import BeautifulSoup #to manipulate html
import pandas as pd #data analysis
import csv #create csv 

wiki_url = "https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture#1920s"
response = requests.get(wiki_url)
#this stores the html content

soup = BeautifulSoup(response.text,'html.parser')
#this parses the HTML content
#table_soup = soup.find_all('table')
#returns list of all tables on wiki page

#print(len(soup.find_all('table')))
#prints number of tables found on wiki page

movie_list = soup.find_all('table',attrs={'class':"wikitable sortable"})
#print((movie_list))
#movie_list2 = soup.find_all('table',attrs={'class':"wikitable"})
#print(len(movie_list2))
#saves the html data that generates tables

headers = [header.text.strip() for header in movie_list[9]('th')]
#stores all headers from the table

rows = []
#initialize empty list

data_rows = movie_list[9].find_all('tr')
#find all the rows using tr tag

for row in data_rows:
    value = row.find_all('td')
    beautified_value = [ele.text.strip() for ele in value]
    # Remove data arrays that are empty
    if len(beautified_value) == 0:
        continue
    rows.append(beautified_value)
#add data from rows into the empty list

with open('movies.csv', 'w', newline="") as output:
    writer = csv.writer(output)
    writer.writerow(headers)
    writer.writerows(rows)

#df = pd.read_html(str(movie_list))
#df = pd.DataFrame(df[0])
#this converts HTML data from string to dataframe

#print(df.head())