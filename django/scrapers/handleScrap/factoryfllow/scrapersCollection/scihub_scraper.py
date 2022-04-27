import sys
import os
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

#"https://sci-hub.se/10.1016/j.respol.2017.12.004"


class SciHub:
    """ science direct scraper """

    url = "https://sci-hub.se/"

    def form_url(self,doi):
        return f'{self.url + doi}'

    def scrape_page(self,url):
        return url
    
    def filter_resault(self,url):
        return url