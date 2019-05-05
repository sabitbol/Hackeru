#!/usr/bin/python
from selenium import webdriver

webpage = "https://www.misim.gov.il/gmIshurim/frmInputMekabel.aspx?cur=0"

driver = webdriver.Chrome()

driver.get(webpage)

inputBox = driver.find_element_by_id("txtMisTik")
inputBox.send_keys("203640701")
submitbtn = driver.find_element_by_id("btnNext")
submitbtn.click()


try:
	driver.find_element_by_id("imgX")
	print "Withholding tax disapproved"
except:
	print "Withholding tax approved"
finally:
	driver.quit()
