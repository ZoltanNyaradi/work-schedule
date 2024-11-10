from django.shortcuts import render
from django.contrib.auth.models import User
import json

# Create your views here.

def schedule(request):
    users = list(User.objects.values('username', 'groups', 'is_staff'))
    return render(request, 'schedule/schedule.html', {'users': json.dumps(users)})