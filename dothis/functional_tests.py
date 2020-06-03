from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome()
	
	def tearDown(self):
		self.driver.quit()

	def test_make_a_task_and_retrieve_it_in_task_list(self):
		self.driver.get("http://localhost:8000")
		
		new_task_button = self.driver.find_element_by_id("new-task-button")
		self.assertEqual(new_task_button.text, "New Task")	
		new_task_button.click()

		self.assertEqual(self.driver.current_url, "http://localhost:8000/task/1/")

		# the lines below don't fill out the form data for the date or status, so the form won't redirect after clicking the submit button. need to figure out how to make selenium  choose a date time and fill out dropdown 
		self.driver.find_element_by_id("title").send_keys("New task.")
		self.driver.find_element_by_id("description").send_keys("This is the description.")

		self.driver.find_element_by_id("Submit").click()

		self.assertEqual(self.driver.current_url, "http://localhost:8000")

		task_list = self.driver.find_elements_by_class_name("task")
		self.assertTrue(
			any(task_list.text == "New Task." for task in task_list)
		)

if __name__ == '__main__':  
    unittest.main(warnings='ignore')
