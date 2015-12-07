# -*- coding: utf-8 -*-
"""
@author: taylorthompson

Module containing functions to open a webpage, source it, parse the html
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from datetime import datetime
import csv

#csv name and searches can be modified by user
CSV_NAME = 'results.csv'  
ROOT_URL = 'http://www.walmart.com/search/'
SEARCHES = ['?query=cereal', '?query=cold%20cereal']

def main():
    ''' opens the csv file, calls the other functions in this module, closes
    the csv file at the end '''
    
    global csv_writer 
    global result_rank
    global keywords
    
    search_results = open(CSV_NAME, 'a')
    csv_writer = csv.writer(search_results, delimiter=',')
    
    for search_term in SEARCHES:
        result_rank = 1
        keywords = re.sub('%20', ' ', search_term[7:])
        source_code = get_source(ROOT_URL + search_term)
        parse_HTML(source_code)
    
    search_results.close()
    
    return 0
    
    
def get_source(URL):
    ''' opens a given url and returns the BeautifulSoup object (essentially 
    a readable html data structure)'''
    
    source = urlopen(URL).read()
    soup = BeautifulSoup(source, "html.parser")
    
    return soup


def parse_HTML(source):
    ''' calls read_results on the given page and checks if there is a link
    to the next page of search results, if there is a next page, opens it and
    recursively calls itself on the next page'''
    
    read_results(source)
    try:
        link = source.find('a', {'class': 'paginator-btn paginator-btn-next'})
        next_page = get_source(ROOT_URL + link['href'])
        parse_HTML(next_page)
    except (AttributeError, TypeError):
        pass
    

def read_results(source):
    ''' takes in a page of search results, prints the search rank, brand name,
    # of reviews, and time of day the search occurred for each result on the 
    page to a .csv file'''
    
    global search_results
    global result_rank
    global keywords
    
    time = datetime.now().strftime('%H:%M')
    
    for product_tile in source.findAll('div', {'class': 
        'js-tile js-tile-landscape tile-landscape'}):
        
        product_title = product_tile.find('a', {'class': 'js-product-title'})
        name = product_title.contents[0]

        if 'Cheerios' in name:
            brand = 'Cheerios'
        elif 'Kashi' in name:
            brand = 'Kashi'
        elif 'Kellogg\'s' in name:
            brand = 'Kellogg\'s'
        elif 'Post' in name:
            brand = 'Post'
        else:
            brand = 'Other'
        
        try:
            temp = product_tile.find('span', 
                {'class': 'stars-reviews'}).contents[0]
            reviews = re.sub('[()]', '', temp)
        except AttributeError:
            reviews = '0'
        
        csv_writer.writerow([brand, result_rank, reviews, time, keywords])
        
        result_rank += 1
        
    return result_rank

main()
# if the above main call is uncommented, this module can be manually executed
