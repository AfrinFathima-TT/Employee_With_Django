from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads



# Create your views here.
class Employee_View(View):
    def get(self, request):

        data = [
            {
                "ID": 1,
                "Name": "Anu",
                "Email": "anu@gmail.com",
                "Mobile": "9876543210",
                "Department": "HR",
                "Designation": "HR Manager",
                "Salary": 35000,
                "Place": "Palakkad"
            },
            {
                "ID": 2,
                "Name": "Neena",
                "Email": "neena@gmail.com",
                "Mobile": "9876543211",
                "Department": "IT",
                "Designation": "Python Developer",
                "Salary": 40000,
                "Place": "Thrissur"
            },
            {
                "ID": 3,
                "Name": "Nayana",
                "Email": "nayana@gmail.com",
                "Mobile": "9876543212",
                "Department": "Finance",
                "Designation": "Accountant",
                "Salary": 30000,
                "Place": "Kochi"
            }
        ]

        return JsonResponse(data, safe=False)
    
@method_decorator(csrf_exempt, name='dispatch')
class Add_Employee_View(View):

    def post(self, request):

        data = request.body
        form_data = loads(data)

        name = form_data.get('name')
        email = form_data.get('email')
        mobile = form_data.get('mobile')
        department = form_data.get('department')
        designation = form_data.get('designation')
        salary = form_data.get('salary')
        place = form_data.get('place')

        employee = {
            "Name": name,
            "Email": email,
            "Mobile": mobile,
            "Department": department,
            "Designation": designation,
            "Salary": salary,
            "Place": place
        }

        return JsonResponse(employee)


@method_decorator(csrf_exempt, name='dispatch')
class Update_Employee_View(View):

    def put(self, request):

        data = request.body
        form_data = loads(data)

        employee_id = form_data.get('id')
        name = form_data.get('name')
        email = form_data.get('email')
        mobile = form_data.get('mobile')
        department = form_data.get('department')
        designation = form_data.get('designation')
        salary = form_data.get('salary')
        place = form_data.get('place')

        employee = {
            "ID": employee_id,
            "Name": name,
            "Email": email,
            "Mobile": mobile,
            "Department": department,
            "Designation": designation,
            "Salary": salary,
            "Place": place
        }

        return JsonResponse(employee)