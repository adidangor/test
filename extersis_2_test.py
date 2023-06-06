from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from statistics import mean
import pytest
import requests
import json
from config import url_ex,url_website_1


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
@pytest.fixture(scope="function")
def get_website():
    driver=webdriver.Chrome('/home/adi2000/chrome driver/chromedriver_linux64/chromedriver',options=options)
    driver.maximize_window()
    return driver

@pytest.fixture(scope="function")
def get_weather_by_zipcode_from_weatherAPI():
    try:
        res = requests.get(url=url_ex)
    except Exception as e:
        return e
    data = json.loads(res.text)
    return data["current"]["temp_f"]

@pytest.fixture(scope="function")
def get_weather_by_zipcode_from_weatherweb(get_website):
    driver=get_website
    driver.get(url_website_1)
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,"#LocationSearch_input").send_keys("20852")
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR,"#LocationSearch_listbox-0").click()
    time.sleep(15)
    temp=driver.find_element(By.CSS_SELECTOR,"#WxuDailyWeatherCard-main-bb1a17e7-dc20-421a-b1b8-c117308c6626 > section > div > ul > li.Column--column--3tAuz.Column--active--27U5T > a > div.Column--temp--1sO_J > span")
    yield int(temp.text[:-1])
    driver.quit()



def test_if_gap_of_10_precents(get_weather_by_zipcode_from_weatherAPI,get_weather_by_zipcode_from_weatherweb):
    counter=abs(get_weather_by_zipcode_from_weatherweb-get_weather_by_zipcode_from_weatherAPI)
    denominator=mean([get_weather_by_zipcode_from_weatherAPI,get_weather_by_zipcode_from_weatherweb])
    result=(counter/denominator)
    assert result <= 0.1 ,"The gap between 2 result grand than 10%"