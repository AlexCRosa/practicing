import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

article_text = soup.find_all("p")

for i in article_text[7:]:
  print(i.text)