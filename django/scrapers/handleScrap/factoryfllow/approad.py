from abc import ABC, abstractmethod
from .string_to_class import *
# importing classes of all scrapers
from .scrapersCollection.sciencedirect_scraper import ScienceDirect
from .scrapersCollection.searchgate_scraper import SearchGate
from .scrapersCollection.scihub_scraper import SciHub

def organize_scraper_data_input(scraper_object):
    """ organize a scraper object to valid input of scraper type """
    scraper = import_string(
        f"django.scrapers.handleScrap.factoryfllow.scrapersCollection.{scraper_object['website'].lower()}_scraper.{scraper_object['website']}")
    params = [scraper_object['key_words'],scraper_object['years']]
    return scraper,params

def organize_scihub_scraper_data_input(doi_string):
    """ organize a scraper object to valid input of scraper type """
    scraper = import_string(
        f"django.scrapers.handleScrap.factoryfllow.scrapersCollection.scihub_scraper.SciHub")
    params = doi_string
    return scraper,params


class scraperType(ABC):
    """ declares the officiale structure of scraper type classes """

    @abstractmethod
    def form_url(self):
        pass

    @abstractmethod
    def scrape_page(self):
        pass
    
    @abstractmethod
    def filter_resaults(self):
        pass



class Road:
    """ a class to define app mechanisem with aplying a factory pattern style"""
    def __init__(self,s:scraperType,params) -> None:
        self.scraper = s
        self.params = params
        self.url = None
        self.resaults = None

    def set_scraper(self):
        self.url = self.scraper.form_url(self.params)
        self.resaults = self.scraper.filter_resaults(
            self.scraper.scrape_page(self.url)
        )


    
def main_activate(scraper_object,type):
    """ main function """
    if type == "scraper":
       new_road = Road(organize_scraper_data_input(scraper_object))
    else:
       new_road = Road(organize_scihub_scraper_data_input(scraper_object))

    new_road.set_scraper()
    return new_road.resaults



## importent meta data:
# all scraper type classes take website and params list as an input 
# and return a dict of wanted data according to kind of scraper