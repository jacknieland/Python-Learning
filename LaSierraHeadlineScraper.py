import requests
import re
from bs4 import BeautifulSoup

# Send HTTP request
html_doc = requests.get('https://lasierra.edu')

# Cook the soup
soup = BeautifulSoup(html_doc.text, 'html.parser')
headlines = str(soup.find_all('h4'))
rx = re.compile('\W+')
tastysoup = rx.sub(' ', headlines).strip()
tastiestsoup = tastysoup.replace("h4", "")
bestsoup = tastiestsoup.split("   ")

for headline in bestsoup:
	print(headline)
