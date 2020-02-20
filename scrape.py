import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.nzherald.co.nz"

def GetHeraldNZArticles():
    response = requests.get(BASE_URL + "/nz/news/headlines.cfm")
    soup = BeautifulSoup(response.text,"html.parser")
    temp_list = soup.select("a[href*='article.cfm']")

    article_list = []
    for i in temp_list:
        item_title = i.text.strip()
        item_url = BASE_URL + i.get("href")
        article_list.append({"title" : item_title, "url" : item_url})
    
    return GetUniqueArticleList(article_list)

def GetUniqueArticleList(duplicate):
    final_list = [] 
    for item in duplicate: 
        if item not in final_list: 
            final_list.append(item) 
    return final_list