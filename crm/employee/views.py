import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from employee.emp_serializer import EmpDeptSerializer
from employee.models import Employees, Departments

# Create your views here.


def home(request):
    content = 'Welcome Employee Services'
    return HttpResponse(content)


@api_view(['POST'])
def add_employee(request):
    import pdb; pdb.set_trace();
    if request.method == 'POST':
        edserializer = EmpDeptSerializer(data=request.POST)
        if edserializer.is_valid():
            emp = Employees()
            emp.first_name = request.POST.get('first_name')
            emp.last_name = request.POST.get('last_name')
            emp.gender = request.POST.get('gender')
            # emp.hire_date = datetime.datetime.now().strftime('%Y-%m-%d')
            # emp.birth_date = datetime.datetime.now().strftime('%Y-%m-%d')
            emp.save(using='employee')

            dept = Departments()
            dept.dept_name = request.POST.get('department')
            dept.dept_id = emp.id
            dept.save(using='employee')

            content = {'message': 'Employee Added Successfully'}
            response = json.dumps(content)
            return HttpResponse(response)
        else:
            content = {'message': 'Employee registrations unsuccessful'}
            response = json.dumps(content)
            return HttpResponse(response)
    else:
        content = {'message': 'User Registration Failed, Please check the fields entered'}
        response = json.dumps(content)
        return HttpResponse(response, content_type="application/json")


@api_view(['GET'])
def show_urls(request, depth=0):
    if request.method == 'GET':
        api_urls = {
            'user_url': 'http://localhost:8005/employee/',
            'user_register_url': 'http://localhost:8005/employee/add_employee',
            'list_users_url': 'http://localhost:8005/employee/list_employees',
            'get_user_url': 'http://localhost:8005/employee/get_employee/{emp_id}',
            'update_user_url': 'http://localhost:8005/employee/update_employee/{emp_id}/dept/{dept_name}',
            'delete_user_url': 'http://localhost:8005/employee/delete_employee/{emp_id}'
        }
        response = json.dumps(api_urls)
        return HttpResponse(response)
    else:
        content = {'message': 'Unable to fetch the data'}
        response = json.dumps(content)
        return HttpResponse(response)


@api_view(['GET'])
def list_Employees(request):
    import pdb; pdb.set_trace();
    if request.method == 'GET':
        employee_data = Employees.objects.using('employee').all()
        list_of_employees = []
        for employee in employee_data:
            dept_id = employee.id
            department_data = Departments.objects.using('employee').get(dept_id=dept_id)
            dept_name = department_data.dept_name
            employees_data = {
                'id': employee.id,
                'name': employee.first_name + ' ' + employee.last_name,
                'gender': employee.gender,
                'department': dept_name,
                'employee_url': 'http://127.0.0.1:8005/employee/get_employee/' + str(employee.id)
            }
            list_of_employees.append(employees_data)

        response = json.dumps(list_of_employees)
        return HttpResponse(response)
    else:
        content = {'message': 'Unable to fetch the data'}
        response = json.dumps(content)
        return HttpResponse(response)


@api_view(['GET'])
def get_employee(request, emp_id):
    import pdb; pdb.set_trace();
    if request.method == 'GET':
        employee_data = Employees.objects.using('employee').get(id=emp_id)
        dept_id = employee_data.id
        department_data = Departments.objects.using('employee').get(dept_id=dept_id)
        dept_name = department_data.dept_name
        employee_info = {
            'id': employee_data.id,
            'name': employee_data.first_name + ' ' + employee_data.last_name,
            'gender': employee_data.gender,
            'department': dept_name
        }

        # employee_info = {}
        # for employee in employee_data:
        #     dept_id = employee.id
        #     department_data = Departments.objects.using('employee').get(dept_id=dept_id)
        #     dept_name = department_data.dept_name
        #     employee_info['id'] = employee.id
        #     employee_info['name'] = employee.first_name + ' ' + employee.last_name,
        #     employee_info['gender'] = employee.gender
        #     employee_info['department'] = dept_name

        response = json.dumps(employee_info)
        return HttpResponse(response)
    else:
        content = {"message": "Not able to fetch the data"}
        response = json.dumps(content)
        return HttpResponse(response)


@api_view(['PUT'])
def update_employee(request, emp_id, dept_name):
    import pdb; pdb.set_trace();
    if request.method == 'PUT':
        employee_data = Departments.objects.using('employee').get(dept_id=emp_id)
        employee_data.dept_name = dept_name
        employee_data.save(using='employee')

        content = {'message': 'Employee Data Updated Successfully'}
        response = json.dumps(content)
        return HttpResponse(response)

    else:
        content = {'message': 'Request not completed, Employee Data Updating Unsuccessful'}
        response = json.dumps(content)
        return HttpResponse(response)


@api_view(['DELETE'])
def delete_employee(request, emp_id):
    if request.method == 'DELETE':
        employee_data = Employees.objects.using('employee').get(id=emp_id)
        employee_data.delete(using='employee')

        content = {'message': 'Employee Deleted Successfully'}
        response = json.dumps(content)
        return HttpResponse(response)

    else:
        content = {'message': 'Request not complete, Unable to Delete'}
        response = json.dumps(content)
        return HttpResponse(response)







