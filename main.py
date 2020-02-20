import requests
import flask
from bs4 import BeautifulSoup

base_url = "https://www.nzherald.co.nz"
response = requests.get(base_url,"/nz/news/headlines.cfm")
soup = BeautifulSoup(response.text,"html.parser")
templist = soup.select("a[href*='article.cfm']")

nz_news_list = []
for i in templist:
    item_title = i.text.strip()
    item_url = base_url + i.get("href")
    nz_news_list.append({item_title,item_url})

print(nz_news_list)