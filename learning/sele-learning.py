
import requests
from bs4 import BeautifulSoup
import csv
import selenium.webdriver as webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC





chrome_driver_path = '/driver/chromedriver'

driver = webdriver.Chrome(chrome_driver_path)

url = 'https://in.puma.com/in/en/mens/mens-new-arrivals'

driver.get(url)

x_path_button = "//button[@class='btn btn-primary show-all-button col-12 col-sm-4 col-md-2 ml-sm-2 ']"


button_to_click = driver.find_element_by_xpath(x_path_button)

webdriverWait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path_button))).click()