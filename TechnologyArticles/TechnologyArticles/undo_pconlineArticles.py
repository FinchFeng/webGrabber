import requests
from bs4 import BeautifulSoup
from dataModel import dataModel

def getPconline():
    dataArray = []
    url = "https://intelligent.pconline.com.cn/"
    result = requests.get(url)
    result.encoding = "gbk"

    # soup = BeautifulSoup(result.text, "html.parser")
    # print(result.text.encode('utf-8').decode('gbk'))
    # div_set = soup.find("div", class_="art-list art-list-cut").find_all("a", class_="img-area")
    print(result.encoding)
    # div_set = soup.findAll("a")
    print(result.text)

    # for div in div_set:
    #     title = div.find("img").get("alt")
    #     eachUrl = div.get("href")
    #     imageUrl = "https://" + div.find("img").get("src")
    #     dataArray.append(dataModel(title, eachUrl, imageUrl, "techArticles"))
    # return dataArray

if __name__ == "__main__":
    array = getPconline()
    # for item in array:
    #     item.printIt()