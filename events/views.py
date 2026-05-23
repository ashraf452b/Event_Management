from django.shortcuts import render
from django.http import HttpResponse
def home_view(request):
    return HttpResponse("Welcome to my project")

def test_view(request):
    return HttpResponse('this is test view')