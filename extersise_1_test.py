from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import chromdriver_path
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
@pytest.fixture(scope="function")
def get_driver():
    driver=webdriver.Chrome(chromdriver_path,options=options)
    driver.maximize_window()
    return driver


def test_convert_between_C_2_F(get_driver):
    driver=get_driver
    driver.get("https://www.metric-conversions.org")
    value_to_convert="30C"
    time.sleep(5)
    send_valued_to_convert=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,"queryFrom")))
    # send_valued_to_convert=driver.find_element(By.NAME,"queryFrom")
    send_valued_to_convert.send_keys(value_to_convert)
    time.sleep(20)
    click_to_convert=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#results > ol > li:nth-child(2) > div > a:nth-child(3)")))
    click_to_convert.click()
    time.sleep(10)
    remove_adb = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ezmob-footer-close")))
    remove_adb.click()
    result_of_converting=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#answer")))
    print(result_of_converting.text)
    driver.quit()

def test_convert_meters_2_fit(get_driver):
    driver=get_driver
    driver.get("https://www.metric-conversions.org")
    time.sleep(20)
    value_to_convert="50"
    driver.find_element(By.CSS_SELECTOR,"#ezmob-footer-close").click()
    ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR,"#mainLinks > a:nth-child(9)")).click().perform()
    enter_data=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#argumentConv")))
    enter_data.send_keys(value_to_convert)
    time.sleep(20)
    remove_adb=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ezmob-footer-close")))
    remove_adb.click()
    change_format =WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#format")))
    change_format.click()
    select = Select(change_format)
    select.select_by_visible_text("Decimal")
    convert_meters_2_fit_answer=driver.find_element(By.ID,"answer")
    print(convert_meters_2_fit_answer.text)
    driver.quit()

def test_convert_ounces_2_grams(get_driver):
    driver=get_driver
    driver.get("https://www.metric-conversions.org")
    time.sleep(20)
    value_to_convert="100"
    weight_form=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#typeMenu > a.typeConv.weight.bluebg")))
    weight_form.click()
    time.sleep(20)
    remove_adb = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ezmob-footer-close")))
    remove_adb.click()
    ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, "#popLinks > ol > li:nth-child(5) > a")).click().perform()
    enter_data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, " #argumentConv")))
    enter_data.send_keys(value_to_convert)
    convert_ounces_2_grams_answer = driver.find_element(By.ID, "answer")
    print(convert_ounces_2_grams_answer.text)
    driver.quit()
