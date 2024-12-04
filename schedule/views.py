from django.shortcuts import render
from django.contrib.auth.models import User
import json

# Form

from .models import Schedule
from django import forms

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ("user",
            "date",
            "begin_of_work_1",
            "end_of_work_1",
            "begin_of_work_2",
            "end_of_work_2",)

# Create your views here.

def schedule(request):
    users = list(User.objects.values('id','username', 'groups', 'is_staff'))
    
    if request.method == "POST":
        schedule_form = ScheduleForm(data=request.POST)
        if schedule_form.is_valid():
            schedule_form.save()
        else:
            print(schedule_form.errors)
    else:
        schedule_form = ScheduleForm()

    return render(
        request,
        'schedule/schedule.html',
        {
            'users': json.dumps(users),
            "schedule_form": schedule_form,
        },
    )