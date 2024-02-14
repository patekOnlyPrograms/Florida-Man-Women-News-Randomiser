from bs4 import *
import lxml
import requests
from selenium import webdriver

url = "https://www.huffpost.com/topic/florida-man?page=1"

response = requests.get(url)


def print_headline(response_text):
    soup = BeautifulSoup(response_text, "lxml")
    headlines = soup.find_all(attrs={"class": "card__headline__text"})
    for headline in headlines:
        if "Florida Man" in headline.text:
            print(headline.text)


print_headline(response.text)

driver_path = "chromedriver"
brave_path = "/usr/bin/brave-browser"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(options=option)

browser.get(url)
