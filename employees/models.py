from django.db import models

# Create your models here.

class Department(models.Model):
	code = models.CharField("Department's Code", max_length=4)
	name = models.CharField("Department's Name", max_length=64)

	def __str__(self):
		return f"{self.code} - {self.name}"

class Employee(models.Model):
	name = models.CharField("Employee's Name", max_length=64, null=False)
	email = models.EmailField("Employee's e-mail", null=False)
	department = models.ForeignKey(Department, on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.name} - {self.email} ({self.department})"

