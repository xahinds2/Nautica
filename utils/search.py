import requests
from bs4 import BeautifulSoup


def flipkart_search(q):

    q = q.replace(" ", "+")
    url = "https://flipkart.dvishal485.workers.dev/search/" + q

    response = requests.get(url, timeout=10)

    product_list = []

    for data in response.json()['result']:
        name = data.get('name', None)
        price = data.get('current_price', None)
        url = data.get('link', None)

        if name and price and url:
            product_data = {
                "title": name,
                "price": price,
                "url": url
            }
            product_list.append(product_data)

    return product_list


def amazon_search(q):

    q = q.replace(" ", "")
    url = 'https://www.amazon.in/s?k=' + q

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_list = []

    raw_data = soup.find_all('div', {'data-component-type': 's-search-result'})

    for data in raw_data:

        name = data.find('span', {'class': 'a-size-medium'})
        price = data.find('span', {'class': 'a-price-whole'})
        url = data.find('a', {'class': 'a-link-normal'})

        if name and price and url:
            product_data = {
                'title': name.text.strip(),
                'price': price.text.strip(),
                'url': 'https://www.amazon.in' + url['href']
            }

            product_list.append(product_data)

    return product_list
