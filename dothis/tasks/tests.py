from django.test import TestCase
from tasks.models import Task

# Create your tests here.
class TaskModelTest(TestCase):
	def test_string_representation(self):
		task = Task(title="Task title")
		self.assertEqual(str(task), task.title)

