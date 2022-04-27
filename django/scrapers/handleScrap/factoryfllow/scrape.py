import requests
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from config import driver



# a function to scrape a site url and get html content
def scrape(url_f):
    try:
      driver.get(url_f)
      time.sleep(7)
      soup = BeautifulSoup(driver.page_source,'html.parser')
      time.sleep(7)
    except Exception as err :
        raise SystemExit(err)
    return soup


# a function that sends request to an api url
def send_req(path):
    """ function to comunicate with the api given a path.. returns response status and json object """
    try:
      r = requests.get(url = path)
      r.raise_for_status()
    except requests.exceptions.HTTPError as err:
      raise SystemExit(err)
    return r
    