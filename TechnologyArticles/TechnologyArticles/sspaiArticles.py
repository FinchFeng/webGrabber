import requests
from dataModel import dataModel

def getSspai():
    url = "https://sspai.com/api/v1/articles?offset=0&limit=20&has_tag=1&tag=%E7%83%AD%E9%97%A8%E6%96%87%E7%AB%A0&include_total=false&type=recommend_to_home"
    list = requests.get(url).json()
    dataArray = []
    llist = list['list']
    for i in range(len(llist)):
        title = llist[i]['title']
        eachUrl = "https://sspai.com/post/" + str(llist[i]['id'])
        imageUrl = "https://cdn.sspai.com/" + llist[i]['banner']
        dataArray.append(dataModel(title,eachUrl,imageUrl,"techArticles"))
    return dataArray

if __name__ == "__main__":
    array = getSspai()
    for item in array:
        item.printIt()