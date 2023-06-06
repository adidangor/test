from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import chromdriver_path, exercise1_website

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


@pytest.fixture(scope="function")
def get_driver():
    # Function that returns the details of the driver
    driver = webdriver.Chrome(chromdriver_path, options=options)
    driver.maximize_window()
    return driver


@pytest.mark.regression
def test_convert_between_C_2_F(get_driver):
    driver = get_driver
    driver.get(exercise1_website)  # The path of the website from the config file
    value_to_convert = "30C"  # A celsius value I chose randomly
    result_converting = "86.00000"  # The result is known in Fahrenheit in advance for 30C
    time.sleep(5)
    # Enter the value_to_convert for converting
    send_valued_to_convert = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "queryFrom")))
    send_valued_to_convert.send_keys(value_to_convert)
    time.sleep(20)
    click_to_convert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#results > ol > li:nth-child(2) > div > a:nth-child(3)")))
    click_to_convert.click()
    time.sleep(10)
    # Remove adb from the website
    remove_adb = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ezmob-footer-close")))
    remove_adb.click()
    # Export the conversion result and check if the result is known in advance to 30C equal to the website result.
    result_of_converting = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#answer")))
    result_of_converting = result_of_converting.text.split("= ")[1][:-2]
    assert result_of_converting == result_converting, "Conversion calculation error"
    driver.close()
    driver.quit()


@pytest.mark.regression
def test_convert_meters_2_fit(get_driver):
    driver = get_driver
    driver.get(exercise1_website)  # The path of the website from the config file
    time.sleep(20)
    value_to_convert = "50"  # A meter value I chose randomly
    result_converting = "164.0420"  # The result is known in fit in advance for 50 meters
    driver.find_element(By.CSS_SELECTOR, "#ezmob-footer-close").click()  # Remove adb from the website
    ActionChains(driver).move_to_element(
        driver.find_element(By.CSS_SELECTOR, "#mainLinks > a:nth-child(9)")).click().perform()

    # Enter the value_to_convert for converting
    enter_data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#argumentConv")))
    enter_data.send_keys(value_to_convert)
    time.sleep(20)
    remove_adb = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ezmob-footer-close")))  # Remove adb from the website
    remove_adb.click()
    # Changing the format of the result
    change_format = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#format")))
    change_format.click()
    select = Select(change_format)
    select.select_by_visible_text("Decimal")
    # Export the conversion result and check if the result is known in advance to 50 meters equal to the website result.
    convert_meters_2_fit_answer = driver.find_element(By.ID, "answer")
    convert_meters_2_fit_answer = convert_meters_2_fit_answer.text.split("= ")[1][:-2]
    print(convert_meters_2_fit_answer)
    assert convert_meters_2_fit_answer == result_converting, "Conversion calculation error"
    driver.close()
    driver.quit()


@pytest.mark.regression
def test_convert_ounces_2_grams(get_driver):
    driver = get_driver
    driver.get(exercise1_website)  # The path of the website from the config file
    time.sleep(20)
    value_to_convert = "100"  # A ounces value I chose randomly
    result_converting = "2834.952"  # The result is known in grams in advance for 100 ounces
    weight_form = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#typeMenu > a.typeConv.weight.bluebg")))
    weight_form.click()
    time.sleep(20)
    remove_adb = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ezmob-footer-close")))  # Remove adb from the website
    remove_adb.click()
    ActionChains(driver).move_to_element(
        driver.find_element(By.CSS_SELECTOR, "#popLinks > ol > li:nth-child(5) > a")).click().perform()
    # Enter the value_to_convert for converting
    enter_data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, " #argumentConv")))
    enter_data.send_keys(value_to_convert)

    # Export the conversion result and check if the result is known in advance to 100 ounces equal to the website result.
    convert_ounces_2_grams_answer = driver.find_element(By.ID, "answer").text
    convert_ounces_2_grams_answer = convert_ounces_2_grams_answer.split("= ")[1][:-1]
    assert convert_ounces_2_grams_answer == result_converting, "Conversion calculation error"
    driver.close()
    driver.quit()
