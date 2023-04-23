import requests
from bs4 import BeautifulSoup
import urllib
from time import sleep


def download_shoe_image(search):
    # search query
    query = clean_query(search)

    # send search query to Google Images
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    response = requests.get(url)
    # parse HTML with Beautiful Soup
    soup = BeautifulSoup(response.text, "html.parser")
    # find URL of first image in search results
    img_elements = soup.find_all("img", class_="yWs4tf")
    # download first image
    if len(img_elements) > 0:
        img_url = img_elements[0]["src"]
        # print(img_url)
        urllib.request.urlretrieve(img_url, f"{search}.jpg")



def clean_query(query):
    return query.replace(" ", "+")

# Testing:
# download_shoe_image("schwama la sportiva womens vegan")

