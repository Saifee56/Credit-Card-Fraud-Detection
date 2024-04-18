
from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
    path('',views.form1,name='form1'),
    path('result',views.form_info,name='result'),
]