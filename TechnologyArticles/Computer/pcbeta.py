import requests
import urllib.request
from bs4 import BeautifulSoup
from dataModel import dataModel

def getPcbeta():
    url = "http://www.pcbeta.com/news/"
    headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read().decode('gbk')
    dataArray = []
    soup = BeautifulSoup(data,"html.parser")
    div_set = soup.find_all("a", class_="thumb")
    for div in div_set:
        if(div.find("img").get("title")):
            title = div.find("img").get("title")
            eachUrl = div.get("href")
            imageUrl = div.find("img").get("src")
            dataArray.append(dataModel(title,eachUrl,imageUrl,"computer"))
    return dataArray

if __name__ == "__main__":
    array = getPcbeta()
    for item in array:
        item.printIt()