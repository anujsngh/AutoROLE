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
from configparser import ConfigParser


cwdir_name = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
projdir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__))).replace('\\', '/')


logging.basicConfig(
    filename="/".join([projdir_name, 'role.log']),
    filemode='w',
    format='%(asctime)s :: %(levelname)s :: %(filename)s ==>  "%(message)s"',
    datefmt='%Y-%m-%d %I:%M:%S%p',
    level=logging.INFO)


def get_config_settings():
    config = ConfigParser()
    config.read("/".join([cwdir_name, "resources/config.ini"]))
    config_dictionary = config
    # print(config_dictionary.sections())
    return config_dictionary


config_dict = get_config_settings()
# print(config_dict.sections())
start_time = config_dict["schedule_settings"]["start_time"]
print(start_time)
end_time = config_dict["schedule_settings"]["end_time"]


# todo: set logging configs here
# todo: import all external packages here
