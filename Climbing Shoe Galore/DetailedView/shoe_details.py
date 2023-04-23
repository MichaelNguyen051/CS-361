from requests_html import HTMLSession
from bs4 import BeautifulSoup


def retrieve_details(shoe_url):
    request = HTMLSession()
    shoe_url = clean_url(shoe_url)
    url = f'https://www.backcountry.com/{shoe_url}'

    response = request.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract first search result
    shoe_details = soup.find('div', {'class': 'css-1h9bni0'}).text.strip()

    return shoe_details

def clean_url(shoe):
    return shoe.replace(" ", "-")


# print(retrieve_details("La sportiva tarantulace climbing shoe"))
