from bs4 import *
import lxml
import requests
from selenium import webdriver
import json

listOfData = []


def headlineFinder(link):
    for pageNumber in range(1, 7, 1):
        url = link + str(pageNumber)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        headlines = soup.find_all(attrs={"class": "card__headline__text"})
        for headline in headlines:
            if "Florida Man" in headline.text:
                listOfData.append([headline.text])


headlineFinder("https://www.huffpost.com/topic/florida-man?page=")

jsonString = json.dumps(listOfData, indent=2)

with open("static/data.json", "w") as outfile:
    outfile.write(jsonString)

print(jsonString)

# Still needs some work
"""def headline_URL(response_text):
    soup = BeautifulSoup(response_text, "lxml")
    linksForHeadlines = soup.find_all(attrs={"class": "card__headline card__headline--long"})
    for linksForHeadline in linksForHeadlines:
            print(linksForHeadline['href'])
"""

driver_path = "chromedriver"
brave_path = "/usr/bin/brave-browser"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

# browser = webdriver.Chrome(options=option)

# browser.get(url)
