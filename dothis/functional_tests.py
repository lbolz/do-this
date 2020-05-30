from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Chrome()
	
	def tearDown(self):
		self.browser.quit()

	def test_start_a_task_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')
		self.assertIn("Do This", self.browser.title)
		self.fail("Need to finish writing the test.")

if __name__ == '__main__':  
    unittest.main(warnings='ignore')
