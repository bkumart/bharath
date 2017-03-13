'''
Created on Mar 11, 2017

@author: BHARATH
'''
from selenium import webdriver
driver=webdriver.Firefox(executable_path="C:/Users/geckodriver.exe")
driver.get("http://gmail.com")
#driver.find_element_by_xpath("//html/body/nav/div/a[2]").click()
driver.find_element_by_name("Email").send_keys("Bharath")
driver.find_element_by_id("next").click()
driver.find_element_by_link_text("Create account").click()
