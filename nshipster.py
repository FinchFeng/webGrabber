import requests
from bs4 import BeautifulSoup
from dataModel import dataModel

def getNshipster():
    dataArray = []
    url = "https://nshipster.com/"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    div_set = soup.find_all("a",class_="title")
    for div in div_set:
        title = div.get_text()
        # eachUrl = "https://www.hackingwithswift.com" + div.get("href")
        # imageUrl = "https://www.hackingwithswift.com" + div.find("img").get("src")
        # dataArray.append(dataModel(title,eachUrl,imageUrl,"swift"))
        print(title)
    return dataArray

if __name__ == "__main__":
    array = getNshipster()
    for item in array:
        item.printIt()