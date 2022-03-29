# pip install -r requirements.txt - 

from bs4 import BeautifulSoup
import requests


def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html,"lxml")
    deputs = soup.find("div", class_ = "grid-deputs")
    deputs_item = deputs.find_all("div", class_ = "dep-item")
    
    deputy_info = []
    for i in deputs_item:
        name = i.find("a", class_ = "name").text
        fraction = i.find("div", class_ = "info").text
        deputy_info.append((name,fraction))
        
    return deputy_info

def main():
    url = "http://kenesh.kg/ky/deputy/list/35"
    html = get_html(url)
    data = get_data(html)
    return data







