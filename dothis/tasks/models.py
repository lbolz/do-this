from django.db import models

# Create your models here.
class Task(models.Model):
	STATUS_CHOICES = (
		("C", "Completed"),
		("I", "Incomplete"),
		("L", "Late"),
		("A", "Abandoned"),
	)

	date = models.DateTimeField("Task date", help_text="Please insert the date and time of the task.")
	title = models.CharField("Task title", max_length=255)
	notes = models.TextField("Task Notes", blank=True, null=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="I")

	def __str__(self):
	 	return self.title
