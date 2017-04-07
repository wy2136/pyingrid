"""
Created on Mon Apr 03, 2017
@author: Wenchang Yang (yang.wenchang@uci.edu)
"""
import requests
from bs4 import BeautifulSoup

def get_data_items(url):
    r = requests.get(url)
    if r.ok is False:
        pass # implement in the future
        return
    htmls = r.text
    indexStart = htmls.find('Datasets and variables')
    indexEnd = htmls.find('Last updated')
    htmls = htmls[indexStart:indexEnd]
    soup = BeautifulSoup(htmls, 'lxml')
    items = {item.text: item.get('href') for item in soup.find_all('a')}

    return items

def nav_datalib():
    '''navigate data library'''

    # dataset selection
    datasets = {
        'CMIP5': 'http://strega.ldeo.columbia.edu:81/CMIP5/',
        'IRIDL': 'http://iridl.ldeo.columbia.edu/SOURCES/',
        'NCEP-NCAR': 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/'}
    dataset_names = sorted( datasets.keys() )
    print('Please select a dataset from the following:')
    for i, dataset_name in enumerate(dataset_names, start=1):
        print('  [{: >1}]{}: {}'.format(i, dataset_name, datasets[dataset_name]))
    print('')
    s = input('>>> Your selection is: ')
    print('')
    dataset_name = dataset_names[int(s) - 1]
    start_url = datasets[dataset_name]

    # data selection
    current_url = start_url
    items = get_data_items(current_url) # items is dict. key=name, value=link
    item_names = sorted(items.keys())
    items_selected = []
    while items:
        print('Please select one item from the following:', end=' ')
        for i, name in enumerate(item_names, start=1):
            if i%5 == 1:
                print('\n', end=' '*4)
            print('[{: >3}]:{}'.format(i, name), end=' ')

        print('\n\nOther options:')
        print(end=' '*4)
        print('[{: >6}]:'.format('Return'), 'Print Current URL')
        print(end=' '*4)
        print('[{: >6}]:'.format(0), 'Go to parent level.')
        print('')

        s = input('>>> Your selection is: ')
        print('')
        if s == '':
            print(current_url)
            return current_url
        elif int(s) == 0:
            if items_selected:
                items_selected.pop()
            else:
                print(current_url)
                return current_url
        else:
            item_name = item_names[int(s) - 1]
            items_selected.append( items[item_name] )
        current_url = start_url + ''.join([item for item in items_selected])
        print('Current URL:')
        print(' '*4 + current_url, end='\n\n')

        items = get_data_items(current_url)
        item_names = sorted(items.keys())

    return current_url
