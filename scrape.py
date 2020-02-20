import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.nzherald.co.nz"

def GetHeraldNZArticles():
    response = requests.get(BASE_URL + "/nz/news/headlines.cfm")
    soup = BeautifulSoup(response.text,"html.parser")
    temp_list = soup.findAll("div", {"class" : "pb-f-homepage-story-feed"})

    article_list = []
    for i in temp_list:
        item_title = i.find("h3").find("a").text
        item_url = BASE_URL + i.find("h3").find("a").get("href")
        item_date = i.find("li", {"class":"timestamp"})
        if(item_date is None):
            article_list.append({"title" : item_title, "url" : item_url, "date" : ""})
        else:
            article_list.append({"title" : item_title, "url" : item_url, "date" : item_date.text})
    
    article_list = sorted(article_list, key = lambda i: i['date'], reverse=True)
    return GetUniqueArticleList(article_list)

def GetUniqueArticleList(duplicate):
    final_list = [] 
    for item in duplicate: 
        if item not in final_list: 
            final_list.append(item) 
    return final_list