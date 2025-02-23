"""Schedule view."""

from django.shortcuts import render
from django.contrib.auth.models import User
import json
from datetime import date, time, datetime
from .forms import ScheduleForm, MessageForm
from .models import Schedule, Message


def schedule(request):
    """
    Handle Post request.

    Schedule editing and message sending.
    Render schedule, messages.
    """
    # Get users
    users = list(User.objects.values('id', 'username', 'groups', 'is_staff'))
    # Get messages
    messages = list(Message.objects.values("user", "created_on", "body"))
    # Get schedules
    schedules = list(Schedule.objects.values(
        "user",
        "date",
        "begin_of_work_1",
        "end_of_work_1",
        "begin_of_work_2",
        "end_of_work_2",
        "sick",
        "vacation"))

    # Change created_on's format suitable for Json
    for message in messages:
        # Convert date to string
        if isinstance(message["created_on"], datetime):
            message["created_on"] = message["created_on"].strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    # Change schedule's date and times' format suitable for Json
    for schedule in schedules:
        if isinstance(schedule["date"], date):
            # Convert date to string
            schedule["date"] = schedule["date"].strftime(
                "%Y-%m-%d"
            )
        if isinstance(schedule["begin_of_work_1"], time):
            # Convert time to string
            schedule["begin_of_work_1"] = schedule["begin_of_work_1"].strftime(
                "%H:%M:%S"
                )
        if isinstance(schedule["end_of_work_1"], time):
            # Convert time to string
            schedule["end_of_work_1"] = schedule["end_of_work_1"].strftime(
                "%H:%M:%S"
                )
        if isinstance(schedule["begin_of_work_2"], time):
            # Convert time to string
            schedule["begin_of_work_2"] = schedule["begin_of_work_2"].strftime(
                "%H:%M:%S"
                )
        if isinstance(schedule["end_of_work_2"], time):
            # Convert time to string
            schedule["end_of_work_2"] = schedule["end_of_work_2"].strftime(
                "%H:%M:%S"
                )

    # Handle post request
    if request.method == "POST":
        # Get from's name from a hidden input
        form_name = request.POST.get("form")

        # Handle edit-schedule-form
        if form_name == "edit-schedule-form":
            # Get which button was clicked
            edit_schedule_crud = request.POST.get("edit-schedule-crud")
            # Get inputs
            s_form = ScheduleForm(data=request.POST)

            # Check that that the form is correctly filled
            if s_form.is_valid():
                # Handle edit button request
                if edit_schedule_crud == "edit":
                    # Check if at least one of these inputs filled
                    con = [
                        s_form.cleaned_data["begin_of_work_1"] is not None,
                        s_form.cleaned_data["end_of_work_1"] is not None,
                        s_form.cleaned_data["sick"] is True,
                        s_form.cleaned_data["vacation"] is True
                    ]

                    if ((con[0] and con[1]) or con[2] or con[3]):
                        # Search for shift with the same date and user
                        existing_schedule = Schedule.objects.filter(
                            user=s_form.cleaned_data["user"].id,
                            date=s_form.cleaned_data["date"]
                        ).first()

                        # If the shift was already existed
                        # then edit it
                        if existing_schedule:
                            var = s_form.cleaned_data["begin_of_work_1"]
                            existing_schedule.begin_of_work_1 = var
                            var = s_form.cleaned_data["end_of_work_1"]
                            existing_schedule.end_of_work_1 = var
                            var = s_form.cleaned_data["begin_of_work_2"]
                            existing_schedule.begin_of_work_2 = var
                            var = s_form.cleaned_data["end_of_work_2"]
                            existing_schedule.end_of_work_2 = var
                            var = s_form.cleaned_data["sick"]
                            existing_schedule.sick = var
                            var = s_form.cleaned_data["vacation"]
                            existing_schedule.vacation = var
                            existing_schedule.save()
                            print("shift updated")

                        # If wasn't then create it
                        else:
                            s_form.save()
                            print("shift created")

                    # Shift is unfilled
                    else:
                        print("shift empty")

                # Handle delete button request
                # Delete schedule
                else:
                    Schedule.objects.filter(
                        user=s_form.cleaned_data["user"].id,
                        date=s_form.cleaned_data["date"]).delete()
                    print("shift deleted")

            # Form is not valid
            else:
                print("form is not valid")

        # Handle message's form
        else:
            print("It's a new message!")
            # Get message form
            message_form = MessageForm(data=request.POST)

            # Check if the form is valid
            if message_form.is_valid():
                print("message form is valid")
                # Save message
                message_form.instance.user = request.user
                message_form.save()

            # The form isn't valid
            else:
                print("message form is not valid")

    # It isn't a Post request
    else:
        s_form = ScheduleForm()
        print("it's not a post")

    # Render schedule and messages
    return render(
        request,
        'schedule/schedule.html',
        {
            'users': json.dumps(users),
            "schedules": json.dumps(schedules),
            "messages": json.dumps(messages),
        },
    )
