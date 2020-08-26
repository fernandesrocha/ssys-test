from django.urls import path, include
from rest_framework import routers
from .api import EmployeeViewSet
from . import views, api

api_router = routers.DefaultRouter()
api_router.register(r"", EmployeeViewSet)

urlpatterns = [
	path("", views.index, name="index"),
    path("employee/", include(api_router.urls)),
	path("employee/<int:employee_id>", views.employee, name="employee"),
	path("employee/add", views.add_employee, name="add_employee"),
	path("employee/<int:employee_id>/delete", views.delete, name="delete")
]