'''
Created on Mar 12, 2017

@author: BHARATH
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox(executable_path="C:/Users/geckodriver.exe")
driver.get("http://www.airindia.in/")
driver.find_element_by_name("from").send_keys("ban")
driver.implicitly_wait(2)
driver.find_element_by_partial_link_text("Bangkok").click()
driver.find_element_by_css_selector("input[id='to']").send_keys("del")
driver.implicitly_wait(2)
driver.find_element_by_link_text("Delhi").click()
dropdown=Select(driver.find_element_by_xpath(".//*[@id='_classType1']"))
dropdown.select_by_index(3)
dropdown.select_by_value("PremiumBusiness")
dropdown.select_by_visible_text("Executive")
