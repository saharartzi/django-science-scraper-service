from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()


#Set the path for your own Science Direct API key
API_KEY = os.getenv("API_KEY")


# setup chrome driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)