from bs4 import *
import lxml
import requests

url = "https://www.huffpost.com/topic/florida-man"

response = requests.get(url)

def print_headline(response_text):
    soup = BeautifulSoup(response_text, "lxml")
    headlines = soup.find_all(attrs={"class": "card__headline__text"})
    for headline in headlines:
        if "Florida Man" in headline.text:
            print(headline.text)

print_headline(response.text)