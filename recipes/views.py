from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# HTTP Request

def my_view(request):
    return render(request,'recipes/home.html')