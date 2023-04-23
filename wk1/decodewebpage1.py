
import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

html_elements = soup.find_all("h3")

article_list = []

for article in html_elements:
    articleTitle = article.text.strip()
    article_list.append(articleTitle)
pprint(article_list)