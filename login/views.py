from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login_to_schedule(request):
  return HttpResponse("<h1 style='background-color:purple;'>Login</h1>")