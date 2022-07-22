#!/usr/bin/python3
from selenium import webdriver
import unittest
class Test(unittest.TestCase):
	def testName(self):
		self.driver=webdriver.Firefox(executable_path="/home/vss9kor/Documents/geckodriver")
		self.driver.get("https://bzo.bosch.com/bzo/en/start_page.html")
#	def testName(self):
		title=self.driver.title
#		self.assertEqual("Bosch-Zünder Online",title,"error loading page")
		self.assertEqual("Bosch-Zünder Online",title,"error loading page")
		print(title)
		self.driver.close()
if __name__=="__main__":
	unittest.main()
