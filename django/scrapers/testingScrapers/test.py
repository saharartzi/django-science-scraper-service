import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models import Scraper, Doi
import unittest
from handleScrap.factoryfllow.approad import main_activate


# here all the testing of scraping will oucure...

def check_if_resault_are_wanted_output(resaults):
    """ a function to iterate all over the resault and check if its the wanted output"""
    for article in resaults:
        if isinstance(article,dict):
            for key, value in article.items():
                if value == 'null' or str or int:
                    return True
        return False

def check_if_all_keys_are_in_resault(resaults):
    for article in resaults:
        if len(article) == 6:
            return True
    return False

def check_if_all_keys_in_dict(resault_dict,num_of_keys):
    if len(resault_dict) == num_of_keys:
        return True
    return False

class TestSearchGateScraper(unittest.TestCase):
    """ a class to test searchgate scraper"""

    scraper_object = Scraper.objects.all().first()
    type_of_scraper = "scraper"

    def test_resault(self) -> None:
        results = main_activate(self.scraper_object,self.type_of_scraper)
        self.assertTrue(isinstance(results, list))
        self.assertTrue(check_if_resault_are_wanted_output(results))
        self.assertTrue(check_if_all_keys_are_in_resault(results))


class TestScienceDirectScraper(unittest.TestCase):
    """ a class to test searchgate scraper"""

    scraper_object = Scraper.objects.all().first()
    type_of_scraper = "scraper"

    def test_resault(self) -> None:
        results = main_activate(self.scraper_object,self.type_of_scraper)
        self.assertTrue(isinstance(results, list))
        self.assertTrue(check_if_resault_are_wanted_output(results))
        self.assertTrue(check_if_all_keys_are_in_resault(results))


class TestSciHubScraper(unittest.TestCase):
    """ a class to test searchgate scraper"""

    scraper_object = Doi.objects.all().first()
    type_of_scraper = "pdf_scraper"

    def test_resault(self) -> None:
        results = main_activate(self.scraper_object,self.type_of_scraper)
        self.assertTrue(isinstance(results, dict))
        self.assertTrue(check_if_all_keys_in_dict(results,2))
        # add more tests to check pdf viability
        


