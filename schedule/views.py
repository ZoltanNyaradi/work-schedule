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
    schedules = list(Schedule.objects.values("user","date"))
    
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
                    existing_schedule.save()

                    is_schedule_exist = True
                    print("qwe")
                    break
            if (not is_schedule_exist):
                print("asd")
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
            "schedule_form": schedule_form,
        },
    )