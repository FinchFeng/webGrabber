import requests
import urllib.request
from bs4 import BeautifulSoup
import re
from dataModel import dataModel
def getAppso():
    url = "https://www.ifanr.com/app"
    result = requests.get(url)
    dataArray = []
    imageArray = []
    i = 0
    soup = BeautifulSoup(result.text, "html.parser")
    div_set = soup.find_all("div", class_="article-info")
    img_set = soup.find_all("a", class_="article-link cover-block")
    for img in img_set:
        txt = str(img['style'])
        # 正则表达式
        p1 = r'https://.*260'
        # 将正则表达式编译成Pattern对象
        pattern = re.compile(p1)
        imageUrl = str(pattern.findall(txt))
        imageArray.append(imageUrl)
    for div in div_set:
        title = div.find("h3").find("a").get_text()
        eachUrl = div.find("h3").find("a").get("href")
        dataArray.append(dataModel(title,eachUrl,imageArray[i],"course"))
        i+=i
    return dataArray

if __name__ == "__main__":
    array = getAppso()
    for item in array:
        item.printIt()