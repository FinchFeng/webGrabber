import requests
from bs4 import BeautifulSoup

def getWebSite():
	url = "https://www.theverge.com/"
	result = requests.get(url)
	soup = BeautifulSoup(result.text)
	div_set = soup.find_all(class_="c-entry-box--compact--hero")
	for div in div_set:
		div2 = div.find(class_="c-entry-box--compact__title")
		text = div2.find("a").get_text()
		print(text)
	# print(soup.prettify())


if __name__ == "__main__":
	getWebSite()


