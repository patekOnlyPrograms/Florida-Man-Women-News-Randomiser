import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
import selenium

url = "https://www.huffpost.com/topic/florida-man"

response = requests.get(url)

def print_headline(response_text):
    keyword = "Florida Man"
    soup = BeautifulSoup(response_text, "lxml")
    headlines = soup.find_all("h3", class_="card__headline__text")
    for headline in headlines:
        if keyword in headline.text:
            print(headline.text)

"""def print_hyperlink(response_text):
    soup = BeautifulSoup(response_text, "html.parser")
    hyperlinks = soup.find_all("a",{"class":"card__headline card__headline--long"})
    for hyperlink in hyperlinks:
        print(hyperlink)"""


print_headline(response.text)
#print_hyperlink(response.text)


# driver = webdriver.Firefox()
# firefox

# using brave browser
driver_path = "chromedriver"
brave_path = "/usr/bin/brave-browser"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(options=option)
browser.get("http://www.python.org")


