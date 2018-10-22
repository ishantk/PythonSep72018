import requests
from bs4 import BeautifulSoup

# Sending the Request and Receiving Response
# response = requests.get("http://zeenews.india.com/")
response = requests.get("https://twitter.com/SrBachchan")

# print(response.text)

soup = BeautifulSoup(response.text,"html.parser")

# print(soup)
# print(type(soup))
# print(soup.prettify())

print("Lets Start Web Scrapping for ")
print(soup.title.text)

print("*****************")
"""
children = soup.children
for child in children:
    print(child)
    print("------------")

print("****************")
"""
print("Latest Tweets by Amitabh Bachchan")
# pTags = soup.find_all('p')
# divTags = soup.find_all('div')
divTags = soup.find_all('div', class_='js-tweet-text-container')

tweets = []

for tag in divTags:
    # print(tag)
    print(tag.text)
    tweets.append(tag.text)
    print("---------------")

print("Total Tweets",tweets.__len__())

# HW: to web scrap various news websites and get the data on GUI using TKinter