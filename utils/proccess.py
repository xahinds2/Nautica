import time
import pandas as pd
from utils.search import flipkart_search, amazon_search


def search_product(q):
    data_list1 = flipkart_search(q)
    data_list2 = amazon_search(q)

    # fix for traffic error
    t_end = time.time() + 10
    while not data_list2 and time.time() < t_end:
        data_list2 = amazon_search(q)

    data_list1.sort(key=lambda x: int(x['price'].replace(',', '')))
    data_list2.sort(key=lambda x: int(x['price'].replace(',', '')))

    data = populate_data(data_list1, data_list2)

    values = list(data.values)
    data.to_csv('logs/datalog.csv')
    return values


def populate_data(query_list1, query_list2):

    df = pd.DataFrame(columns=['SL No.', 'Title', 'Price', 'Title', 'Price'])

    for i in range(10):
        if i < len(query_list1) and i < len(query_list2):
            item1 = query_list1[i]
            item2 = query_list2[i]
            df.loc[len(df)] = [i+1, item1['title'], item1['price'], item2['title'], item2['price']]

        elif i < len(query_list1):
            item1 = query_list1[i]
            df.loc[len(df)] = [i+1, item1['title'], item1['price'], 'NA', 'NA']

        elif i < len(query_list2):
            item2 = query_list2[i]
            df.loc[len(df)] = [i+1, 'NA', 'NA', item2['title'], item2['price']]

    return df
