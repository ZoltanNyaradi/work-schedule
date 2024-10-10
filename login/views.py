from django.shortcuts import render

# Create your views here.

def login_to_schedule(request):
    return render(request, 'login/login.html')