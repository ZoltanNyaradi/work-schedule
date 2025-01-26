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