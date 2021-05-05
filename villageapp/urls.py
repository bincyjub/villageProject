from . import views
from django.urls import path



app_name = 'villageapp'

urlpatterns = [
	path('',views.index,name='index'),
	path('register_panchayath/',views.register_panchayath,name='register_panchayath'),
    path('register_employees/',views.register_employees,name='register_employees')

]