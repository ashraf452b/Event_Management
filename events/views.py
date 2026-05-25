from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request,'home.html')

def test_view(request):
    return HttpResponse('this is test view')