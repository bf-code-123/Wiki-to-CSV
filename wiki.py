import requests #to manipulate web page
from bs4 import BeautifulSoup #to manipulate html
import pandas as pd #data analysis

wiki_url = "https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture#2010s"
response = requests.get(wiki_url)

test_soup = BeautifulSoup(response.text,'html.parset')
movie_list = test_soup.find('table')