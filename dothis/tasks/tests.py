from django.urls import resolve
from django.test import TestCase
from tasks.models import Task

from tasks.views import task_list

# Create your tests here.
class TaskListPageTest(TestCase):
	def test_root_url_resolves_to_task_list_view(self):
		found = resolve('/')
		self.assertEqual(found.func, task_list)

class TaskModelTest(TestCase):
	def test_string_representation(self):
		task = Task(title="Task title")
		self.assertEqual(str(task), task.title)

