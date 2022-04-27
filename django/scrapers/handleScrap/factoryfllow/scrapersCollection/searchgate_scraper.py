import urllib.parse
import re
import os
import sys
from selenium.common.exceptions import NoSuchElementException


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# importing frame script
from ..scrape import scrape


class SearchGate:
    """ search gate scraper """

    url = 'https://www.researchgate.net/search/publication?'

    def form_url(self,params):
        query_params = {'q':params[0]} 
        return self.url + urllib.parse.urlencode(query_params)

    def scrape_page(self,final_url):
        return scrape(final_url)  

    def filter_resault(self,returned_content):
        return self.find_results(returned_content)
        

def find_results(returned_content):    
    try:
        list_resault = []
        for div in returned_content.soup.findAll('div', attrs={'class':'search-results-container js-search-results-container'}):
            resault_dict = {}
            link_tag = div.find('a')
            resault_dict['link'] = link_tag['href'].split('/')[1]
            resault_dict['title'] = link_tag.text
            data = div.find('div', attrs={'class':'nova-legacy-v-publication-item__meta'})
            resault_dict['details'] = data.text
            authors = div.find('ul', attrs={'class':'nova-legacy-e-list nova-legacy-e-list--size-m nova-legacy-e-list--type-inline nova-legacy-e-list--spacing-none nova-legacy-v-publication-item__person-list'})
            resault_dict['authors'] = [author.text for author in authors.findAll('li', attrs={'class':'nova-legacy-e-list__item'})]
            resault_dict['date'] = 'null'
            resault_dict['cites'] = 'null'
            list_resault.append(resault_dict)

        return list_resault
        
    except NoSuchElementException:  
        print("An error ocurrd")



