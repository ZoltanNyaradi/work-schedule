from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.serializers import serialize
from django.core.serializers import serialize
import json
from datetime import date, time, datetime

# Form

from .models import Schedule, Message
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

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("body",)

# Create your views here.

def schedule(request):
    users = list(User.objects.values('id','username', 'groups', 'is_staff'))
    messages = list(Message.objects.values("user", "created_on" , "body"))
    schedules = list(Schedule.objects.values(
        "user",
        "date",
        "begin_of_work_1",
        "end_of_work_1",
        "begin_of_work_2",
        "end_of_work_2",
        "sick",
        "vacation"))

    for message in messages:
        if isinstance(message["created_on"], datetime):  # Convert date to string
            message["created_on"] = message["created_on"].strftime("%Y-%m-%d/%H:%M:%S")
    
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
        form_name = request.POST.get("form")
        if form_name == "schedule":
            edit_schedule_crud = request.POST.get("edit-schedule-crud")
            schedule_form = ScheduleForm(data=request.POST)

            if schedule_form.is_valid():    
                if edit_schedule_crud == "edit":
                    print(schedule_form.cleaned_data["begin_of_work_2"])
                    if ((schedule_form.cleaned_data["begin_of_work_1"] != None
                        and schedule_form.cleaned_data["end_of_work_1"] != None)
                        or schedule_form.cleaned_data["sick"] == True
                        or schedule_form.cleaned_data["vacation"] == True
                    ):
                        existing_schedule = Schedule.objects.filter(
                            user=schedule_form.cleaned_data["user"].id,
                            date=schedule_form.cleaned_data["date"]
                        ).first()
                        print(existing_schedule)
                        if existing_schedule:
                            existing_schedule.begin_of_work_1 = schedule_form.cleaned_data["begin_of_work_1"]
                            existing_schedule.end_of_work_1 = schedule_form.cleaned_data["end_of_work_1"]
                            existing_schedule.begin_of_work_2 = schedule_form.cleaned_data["begin_of_work_2"]
                            existing_schedule.end_of_work_2 = schedule_form.cleaned_data["end_of_work_2"]
                            existing_schedule.sick = schedule_form.cleaned_data["sick"]
                            existing_schedule.vacation = schedule_form.cleaned_data["vacation"]
                            existing_schedule.save()
                            print("shift updated")
                               
                        else:
                            schedule_form.save()
                            print("shift created")
                    else:
                        print("shift empty")
                else:
                    Schedule.objects.filter(
                        user = schedule_form.cleaned_data["user"].id,
                        date = schedule_form.cleaned_data["date"]).delete()
                    print("shift deleted")

            else:
                print("form is not valid") 
        else:
            schedule_form = ScheduleForm()
            print("It's a new message!")

            message_form = MessageForm(data=request.POST)

            if message_form.is_valid():
                print("message form is valid")
                message_form.instance.user = request.user 
                message_form.save()
            else:
                print("message form is not valid")
    else:
        schedule_form = ScheduleForm()
        print("it's not a post")


    return render(
        request,
        'schedule/schedule.html',
        {
            'users': json.dumps(users),
            "schedules": json.dumps(schedules),
            "messages":json.dumps(messages),
            "schedule_form": schedule_form,
        },
    )