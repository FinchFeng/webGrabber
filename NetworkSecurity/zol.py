import re
import requests
from bs4 import BeautifulSoup
from dataModel import dataModel

def getZol():
    dataArray = []
    url = "http://safe.zol.com.cn/more/2_1628.shtml"
    data = requests.get(url)
    # headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45")
    # opener = urllib.request.build_opener()
    # opener.addheaders = [headers]
    # data = opener.open(url).read().decode('iso-8859-1')
    soup = BeautifulSoup(data.text, "html.parser")
    div_set = soup.find_all("div", class_="info-mod clearfix")
    for div in div_set:
        title = div.find("a").find("img").get("alt")
        eachUrl = div.find("a").get("href")
        if(div.find("a").find("img").get(".src") != None):
            imageUrl = div.find("a").find("img").get(".src")
        else:
            imageUrl = div.find("a").find("img").get("src")
        dataArray.append(dataModel(title, eachUrl, imageUrl, "networkSecurity"))
    return dataArray

if __name__ == "__main__":
    array = getZol()
    for item in array:
        item.printIt()