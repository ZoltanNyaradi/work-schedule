from django.shortcuts import render
from django.contrib.auth.models import User
import json
from datetime import date, time

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
            "end_of_work_2",
            "sick",
            "vacation")

# Create your views here.

def schedule(request):
    users = list(User.objects.values('id','username', 'groups', 'is_staff'))
    schedules = list(Schedule.objects.values(
        "user",
        "date",
        "begin_of_work_1",
        "end_of_work_1",
        "begin_of_work_2",
        "end_of_work_2",
        "sick",
        "vacation"))
    
    for schedule in schedules:
        if isinstance(schedule["date"], date):  # Convert date to string
            schedule["date"] = schedule["date"].strftime("%Y-%m-%d")
        if isinstance(schedule["begin_of_work_1"], time):  # Convert time to string
            schedule["begin_of_work_1"] = schedule["begin_of_work_1"].strftime("%H:%M:%S")
        if isinstance(schedule["end_of_work_1"], time):  # Convert time to string
            schedule["end_of_work_1"] = schedule["end_of_work_1"].strftime("%H:%M:%S")
        if isinstance(schedule["begin_of_work_2"], time):  # Convert time to string
            schedule["begin_of_work_2"] = schedule["begin_of_work_2"].strftime("%H:%M:%S")
        if isinstance(schedule["end_of_work_2"], time):  # Convert time to string
            schedule["end_of_work_2"] = schedule["end_of_work_2"].strftime("%H:%M:%S")

    if request.method == "POST":
        schedule_form = ScheduleForm(data=request.POST)
        if schedule_form.is_valid():           
            is_schedule_exist = False
            for schedule in schedules:
                if (
                    schedule["user"] == schedule_form.cleaned_data["user"].id and
                    schedule["date"] == schedule_form.cleaned_data["date"]
                ):
                    existing_schedule = Schedule.objects.filter(
                        user=schedule_form.cleaned_data["user"].id,
                        date=schedule_form.cleaned_data["date"]).first()
                    existing_schedule.begin_of_work_1 = schedule_form.cleaned_data["begin_of_work_1"]
                    existing_schedule.end_of_work_1 = schedule_form.cleaned_data["end_of_work_1"]
                    existing_schedule.begin_of_work_2 = schedule_form.cleaned_data["begin_of_work_2"]
                    existing_schedule.end_of_work_2 = schedule_form.cleaned_data["end_of_work_2"]
                    existing_schedule.sick = schedule_form.cleaned_data["sick"]
                    existing_schedule.vacation = schedule_form.cleaned_data["vacation"]
                    existing_schedule.save()

                    is_schedule_exist = True
                    
                    break
            if (not is_schedule_exist):
                
                schedule_form.save()
#Schedule.objects.filter(
#                        user=schedule_form.cleaned_data["user"].id,
#                        date=schedule_form.cleaned_data["date"]).delete()
        else:
            print(schedule_form.errors)
    else:
        schedule_form = ScheduleForm()

    return render(
        request,
        'schedule/schedule.html',
        {
            'users': json.dumps(users),
            "schedules": json.dumps(schedules),
            "schedule_form": schedule_form,
        },
    )