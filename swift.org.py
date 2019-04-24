import requests
from bs4 import BeautifulSoup
from dataModel import dataModel

def getSwiftOrg():
    dataArray = []
    url = "https://swift.org/blog/"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    div_set = soup.find_all("h1",class_="title")
    for div in div_set:
        title = div.get_text()
        eachUrl = "https://swift.org/blog/" + div.get_text("href")
        # imageUrl = "https://www.hackingwithswift.com" + div.find("img").get("src")
        imageUrl = None
        dataArray.append(dataModel(title,eachUrl,imageUrl,"swift"))
    return dataArray

if __name__ == "__main__":
    array = getSwiftOrg()
    for item in array:
        item.printIt()