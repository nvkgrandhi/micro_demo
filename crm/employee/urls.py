from django.conf.urls import url, include, patterns
from employee import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^show_urls/', views.show_urls, name='show_urls'),
    url(r'^add_employee/', views.add_employee, name='add_employee'),
    url(r'^list_employees/', views.list_Employees, name='list_Employees'),
    url(r'^get_employee/(?P<emp_id>\d+)$', views.get_employee, name='get_employee'),
    url(r'^update_employee/(?P<emp_id>\d+)/dept/(?P<dept_name>\w+)$', views.update_employee, name='update_employee'),
    url(r'^delete_employee/(?P<emp_id>\d+)$', views.delete_employee, name='delete_employee'),
]