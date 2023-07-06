import pandas as pd


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