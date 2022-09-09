from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import requests
import time
import os
import sys
sys.path.append("/home/tewer/Web_Project/data")
import pythonHw2 as p2
import pythonHw3 as p3
import pythonHw4 as p4


def scrap(data):
    URL = "https://wormbase.org/species/c_elegans/transcript/"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning) 
    PATH = "/home/tewer/Desktop/C++/chromedriver"
    transcript = data
    input = "//input[@id='basic-search-input']"
    submit = "//div[@id='basic_search-content']/form[1]/input[@type='submit']"
    res = "//*[@id='results']/ul/div[2]/li/span[2]/a"
    file = "//*[@id='ui-id-2']/div/div[2]/div/button[2]"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs",{"download.default_directory" : "/home/tewer/Web_Project/downloadFiles"})
    driver = webdriver.Chrome(executable_path=PATH,options=chrome_options) 

    params = {"behavior":"allow", "downloadPath": os.getcwd()}
    driver.execute_cdp_cmd("Page.setDownloadBehavior", params)

    driver.get("https://wormbase.org/species/c_elegans/transcript/")
    driver.find_element(By.XPATH,input).send_keys(transcript)
    driver.find_element(By.XPATH,submit).submit()
    time.sleep(5)
    driver.find_element(By.XPATH,res).click()
    # time.sleep(3)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # time.sleep(3)

    data1 = driver.find_element(By.XPATH,file)
    # try:
    driver.execute_script("arguments[0].click();", data1)
    time.sleep(5)
    #HW 2: 
    p2.displayAll(transcript)
    #HW 3:
    p3.ExonOnly(transcript)
    #HW 4:
    p4.CDS(transcript)
    
    if os.path.exists("/home/tewer/Web_Project/unspliced+UTRTranscriptSequence_{}.fasta".format(transcript)):
        os.remove("/home/tewer/Web_Project/unspliced+UTRTranscriptSequence_{}.fasta".format(transcript))
    # else:
        # print("No such file")
    # except:
        # print("Something is wrong")
    driver.close()

# scrap("H03G16.7.1")



