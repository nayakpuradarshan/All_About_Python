from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook – log in or sign up" in driver.title
elem = driver.find_element_by_id("email")
elem.clear()
elem.send_keys("xxxxxxxx")
elem = driver.find_element_by_id("xxxxx")
elem.send_keys("aoldday")
elem = driver.find_element_by_xpath("//*[@id='u_0_2']")
elem.click()
time.sleep(30)
elem = driver.find_element_by_xpath('//*[@id="js_a"]')
elem.clear()
elem.send_keys("Hello, This is automated post!!")
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div/button/span').click()
driver.close()