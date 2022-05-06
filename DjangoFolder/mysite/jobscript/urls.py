
from django.urls import path

from . import views

app_name = 'jobscript'
urlpatterns = [
    path('', views.index, name='index'),

]
