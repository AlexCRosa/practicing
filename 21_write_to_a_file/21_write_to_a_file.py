import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
title = soup.find_all('h3', {'class': 'indicate-hover'})

file_name = input("What's the file name? ")
    
with open(f'{file_name}.txt', 'w') as open_file:
    for i in title:
        open_file.write(f'{i.text}\n')
    open_file.close()