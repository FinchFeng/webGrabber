import requests
from bs4 import BeautifulSoup
from dataModel import dataModel

def getIgao7():
    dataArray = []
    imageurlArray = []
    i = 0
    url = "http://m.igao7.com/category/all"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    img_set = soup.find_all("div",class_="pic")
    for img in img_set:
        imageurlArray.append(img.find("img").get("src"))
    div_set = soup.find_all("div",class_="name clr")
    for div in div_set:
        title = div.find("span",class_="hd").get_text()
        eachUrl = div.parent.get("href")
        dataArray.append(dataModel(title,eachUrl,imageurlArray[i],"phone"))
        ++i
    return dataArray

if __name__ == "__main__":
    array = getIgao7()
    for item in array:
        item.printIt()