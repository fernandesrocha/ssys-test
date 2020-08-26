from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .serializers import EmployeeSerializer
from .models import Employee, Department
from .forms import *
from .api import EmployeeViewSet

# Create your views here.

# Listing func
def index(request):
	context = {
		"employees": Employee.objects.all()
	}
	return render(request, "employees/index.html", context)

# Detailing func
def employee(request, employee_id):
	#testing employee_id in DB
	try:
		employee = Employee.objects.get(pk=employee_id)
	except Employee.DoesNotExits:
		raise Http404("Employee does not exist!")
	context = {
		"employee": employee
	}
	return render(request, "employees/employee.html", context)

def add_employee(request):
	# POST response
	if request.method == 'POST':
		form = EmployeeForm(request.POST)

		if form.is_valid():
			new_employee = form.save()
			new_employee.save()

			context = {
				"employees": Employee.objects.all()
			}
		return redirect('employee', employee_id=new_employee.pk)
	# GET response
	else:
		form = EmployeeForm() # forms.py
		return render(request, "employees/add_employee.html", {'form':form})

def delete(request, employee_id):
	try:
		employee = Employee.objects.get(pk=employee_id)
	except Employee.DoesNotExits:
		raise Http404("Employee does not exist!")

	if request.method == 'POST':
		if 'confirm' in request.POST:
			employee.delete()
			context = {
				"employees": Employee.objects.all()
			}
			return redirect('index')
		else: # user CANCELED
			return redirect('employee', employee_id=employee.pk)
	else: #method == 'GET'
		context = {
			"employee": employee
		}
		return render(request, "employees/del_confirm.html", context)