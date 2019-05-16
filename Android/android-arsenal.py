
import requests
from bs4 import BeautifulSoup
from dataModel import dataModel

def getAndroidArsenal():
    dataArray = []
    url = "https://android-arsenal.com/?sort=updated"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    div_set = soup.find_all("div", class_="pi")
    for div in div_set:
        if(div.find("div").find("div").find("a")):
            title = div.find("div").find("div").find("a").get_text()
            # print(title)
            eachUrl = "https://android-arsenal.com" + div.find("a").get("href")
            # print(eachUrl)
            # if(div.find("div").find_next_sibling().find("p").find_next_sibling()):
            #     print(div.find("div").find_next_sibling().find("p").find_next_sibling().find("img"))
            # else:
            #     print("N")
            img = div.find("div").find_next_sibling().find("p").find_next_sibling()
            if(img):
                if(img.find("img")):
                    imageUrl = img.find("img").get("data-layzr")
                else:
                    imageUrl = None
            else:
                imageUrl = None
            dataArray.append(dataModel(title, eachUrl, imageUrl, "android"))
    return dataArray

if __name__ == "__main__":
    array = getAndroidArsenal()
    for item in array:
        item.printIt()