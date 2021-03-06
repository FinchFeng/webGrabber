import requests
import re
from bs4 import BeautifulSoup
from dataModel import dataModel

def getSouhu():
    dataArray = []
    imageUrlArray = []
    i = 0
    url = "http://www.sohu.com/tag/59740?spm=smpc.ch30.fd-ctag.20.1556018818504jdhznyH"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    div_set = soup.find_all(attrs={"data-role":"news-item"})
    for img in div_set:
        txt = str(img['class'])
        # 正则表达式
        p1 = r'txt'
        # 将正则表达式编译成Pattern对象
        pattern = re.compile(p1)
        if(pattern.findall(txt)):
            noImg = None
            imageUrlArray.append(noImg)
        else:
            otherImg = "https://" + img.find("img").get("src")
            imageUrlArray.append(otherImg)
        title = img.find("h4").find("a").get_text().strip()
        eachUrl = "https:"+img.find("h4").find("a").get("href")
        dataArray.append(dataModel(title,eachUrl,imageUrlArray[i],"phone"))
        i += 1
    return dataArray

if __name__ == "__main__":
    array = getSouhu()
    for item in array:
        item.printIt()