from django.shortcuts import render
from .models import Task

# Create your views here.
def task_list(request):
	task_list = Task.objects.all()
	context = {
		"task_list": task_list
	}
	return render(request, "tasks/task_list.html", context)

def calendar(request):
	context = {}
	return render(request, "tasks/calendar.html", context)
