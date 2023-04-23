from requests_html import HTMLSession
from bs4 import BeautifulSoup


def retrieve_shoe_list(brand, type=None, closure=None):
    request = HTMLSession()
    url = "https://www.backcountry.com/climbing-shoes"
    if brand == "La Sportiva":
        filtered_url = url + "?p=Brand%3A120"
    elif brand == "Scarpa":
        filtered_url = url + "?p=Brand%3A100000327"
    elif brand == "Evolv":
        filtered_url = url + "?p=Brand%3A100000486"
    else:
        print("Error")

    response = request.get(filtered_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract first search result
    shoe_name = soup.find_all("h2", attrs={'class': 'chakra-heading css-1gfqank'})
    shoe_list = []
    for shoe in shoe_name:
        shoe_list.append(shoe.text)

    return shoe_list

# print(retrieve_shoe_list("La Sportiva"))
