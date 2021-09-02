import os
import time
import logging
import schedule
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup
from selenium import webdriver
from plyer import notification
from selenium.webdriver.chrome.service import Service


logging.basicConfig(
    filename='../role.log',
    filemode='w',
    format='%(asctime)s :: %(levelname)s :: %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S%p',
    level=logging.INFO)


# todo: set logging configs here
# todo: import all external packages here
