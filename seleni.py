#!/usr/bin/python3
from selenium import webdriver
import unittest
class Test(unittest.TestCase):
	def testName(self):
		self.driver=webdriver.Firefox(executable_path="/home/Documents/geckodriver")
		self.driver.get("https//:google.com")
#	def testName(self):
		title=self.driver.title
#		self.assertEqual("Google",title,"error loading page")
		self.assertEqual("Google",title,"error loading page")
		print(title)
		self.driver.close()
if __name__=="__main__":
	unittest.main()
