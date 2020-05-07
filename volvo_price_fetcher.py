import re
import requests
from bs4 import BeautifulSoup

# scrapes blocket.se for Volvo cars from year >= 2000 (excluding leasing), saves (year,price) to file

base_url = 'https://www.blocket.se/annonser/hela_sverige/fordon/bilar?cb=41&cg=1020&mys=2000&pl=0&page='

# how many pages are there?
response = requests.get(f"{base_url}{str(9999)}")
pages = int(re.search("page=(.+?)&", response.url).group(1))

f = open("volvo.csv", "a")

for page in range(1,pages+1):
	url = base_url + str(page)
	print(url)
	response = requests.get(url)

	soup = BeautifulSoup(response.text, "html.parser")

	cars = soup.findAll("div", {"class": "hdKKry"})
	for car in cars:
		year = car.find("li", {"class": "bQxiZq"}).text
		price = car.find("div", {"class": "bcaUdR"}).text.replace(" ", "").split('kr',1)[0]
		f.write(f"{year},{price}\n")
f.close()