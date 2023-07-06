import requests
from bs4 import BeautifulSoup


def flipkartSearch(q):

    q = q.replace(" ", "+")
    url = "https://www.flipkart.com/search?q=" + q

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    product_list = []

    raw_data = soup.find_all("div", class_="_2kHMtA")

    for data in raw_data:
        name = data.find("div", class_="_4rR01T")
        price = data.find("div", class_="_30jeq3 _1_WHN1")
        url = data.find("a", class_="_1fQZEK")

        if name and price and url:
            product_data = {
                "title": name.text,
                "price": price.text[1:],
                "url": "https://www.flipkart.com" + url["href"]
            }
            product_list.append(product_data)

    return product_list


def amazonSearch(q):

    q = q.replace(" ", "")
    url = 'https://www.amazon.in/s?k=' + q

    response = requests.get(url)
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
