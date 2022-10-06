from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests
import pandas as pd

url=("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG")
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
titles = []
costs = []
ratings = []
links=[]
names = soup.find_all('div', class_="_4rR01T")
prices = soup.find_all('div', class_="_30jeq3 _1_WHN1")
stars = soup.find_all('div', class_="_3LWZlK")
products = soup.find_all('a', class_="_1fQZEK")
for name in names:
    titles.append(name.text)
for price in prices:
    costs.append(price.text)
for star in stars:
    ratings.append(star.text)
for product in products:
    links.append(product.get('href'))
dataset = pd.DataFrame()
dataset['mobile_name'] = titles
dataset['price'] = costs
dataset['ratings'] = ratings
dataset['links']= links
dataset.to_excel("scrape.xlsx")

    
    

    