'''
Created on Mar 11, 2017

@author: BHARATH
'''
from selenium import webdriver
driver=webdriver.Firefox(executable_path="C:/Users/geckodriver.exe")
driver.get("http://facebook.com")
#driver.find_element_by_xpath(".//*[@id='u_0_q']").click()
driver.find_element_by_xpath(".//*[@id='u_0_6']").send_keys("xpathdemo")
driver.find_element_by_css_selector("#u_0_q").click()