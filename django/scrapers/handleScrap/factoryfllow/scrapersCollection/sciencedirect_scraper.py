import sys
import os
import urllib.parse
from ..config import API_KEY

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# importing frame script
from ..scrape import send_req


class ScienceDirect:
    """ science direct scraper """

    url = 'http://api.elsevier.com/content/search/scopus?'

    def form_url(self,params):
        query_params = {'query':params[0],'date':params[1], 'apikey':API_KEY}
        return self.url + urllib.parse.urlencode(query_params)

    def scrape_page(self,final_url):
        return send_req(final_url)  

    def filter_resault(self,returned_content):
        return ResponseParser.bring_title(ResponseParser.load_json_object(returned_content))


class ResponseParser:
    """a class to parse json response from science api"""
    
    def load_json_object(response):
        return response.json()

    def bring_title(loaded_json):
        article_list = [{
        'title': article['dc:title'],
        'link': article['link'][2]['@href'],
        'author': article['dc:creator'],
        'details': article['prism:publicationName']+article['affiliation'][0]['affilname'],
        'date': article['prism:coverDisplayDate'],
        'cited-count': article['citedby-count'],
        }
        for article in loaded_json['search-results']['entry']]
        return article_list

