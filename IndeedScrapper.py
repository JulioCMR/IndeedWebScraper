from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

driver.get("https://mx.indeed.com/")
