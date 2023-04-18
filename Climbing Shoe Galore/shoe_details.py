from requests_html import HTMLSession
from bs4 import BeautifulSoup

request = HTMLSession()
# url = f'https://www.amazon.com/s?k={search_query}'
url = 'https://www.backcountry.com/mad-rock-drone-comp-series-high-volume-climbing-shoe'

response = request.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# Extract first search result
# result = soup.find('div', {'class': 'a-section a-spacing-small puis-padding-left-small puis-padding-right-small'})
product_name = soup.find('div', {'class': 'css-1h9bni0'}).text.strip()
# product_price = result.find('span', {'class': 'a-offscreen'}).text.strip()
# print(result)

# Print product name and price
print(f'Product Name: {product_name}')
# print(f'Product Price: {product_price}')
