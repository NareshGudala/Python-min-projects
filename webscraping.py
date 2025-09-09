import requests
from bs4 import BeautifulSoup
import pandas as pd

# Kaggle website
# response = requests.get("https://www.kaggle.com/")

# Amazon website
response = requests.get("https://www.flipkart.com/apple-iphone-14-plus-blue-128-gb/p/itmac8385391b02b?pid=MOBGHWFHUYWGB5F2&lid=LSTMOBGHWFHUYWGB5F2XIJVA7&marketplace=FLIPKART&q=apple+mobiles&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&fm=search-autosuggest&iid=fa072e8a-4143-48e8-8da4-728a9152195f.MOBGHWFHUYWGB5F2.SEARCH&ppt=clp&ppn=samsung-mobile-store&ssid=r5seogsfz40000001721406243277&qH=cb603b9543d774e1")
# print(response)

soup = BeautifulSoup(response.content,'html.parser') 
'''
parser -> It is convertion or Reader

print(soup) -> It's will get website data or webscraping in unstructure data
'''
print(soup)

names = soup.find_all('div',class_="VU-ZEz")
print(names)

# for name in names:
#     print(name.text)
