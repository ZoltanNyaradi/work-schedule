"""Create classes for froms."""

from .models import Schedule, Message
from django import forms


class ScheduleForm(forms.ModelForm):
    """Form model for Edit-Schedule."""

    class Meta:
        """Metadata for ScheduleForm."""

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
    """Form model for Messages."""

    class Meta:
        """Metadata for MessageForm."""

        model = Message
        fields = ("body",)
