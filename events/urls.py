# from django.contrib import admin
from django.urls import path,include
from events.views import  home_view,test_view

urlpatterns = [
    path('test_view/',test_view,name='test-view'),
]