'''
Created on Mar 11, 2017

@author: BHARATH
'''
from selenium import webdriver
driver=webdriver.Firefox(executable_path="C:/Users/geckodriver.exe")
driver.get("http://facebook.com")
#Name Attribute
driver.find_element_by_name("firstname").send_keys("Bharath")
#ID Attribute
driver.find_element_by_id("u_0_3").send_keys("Kumar")
#Class Attribute
driver.find_element_by_id("u_0_q").click()
driver.find_element_by_link_text("Forgot account?").click()