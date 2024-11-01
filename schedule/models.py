from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Message(models.Model):
  """
  Model for storing messages.
  """
  user = models.ForeignKey(
    User,
    on_delete=models.PROTECT,
    related_name="message_writer")
  created_on = models.DateTimeField(auto_now_add=True)
  body = models.TextField()


class Schedule(models.Model):
  """
  Model for storing schedules.
  Stores the day the releted user,
  and one or two starting and finishing time.
  """
  user = models.ForeignKey(
    User,
    on_delete=models.PROTECT,
    related_name="worker")
  date = models.DateField()
  begin_of_work_1 = models.TimeField()
  end_of_work_1 = models.TimeField()
  begin_of_work_2 = models.TimeField(null=True, blank=True)
  end_of_work_2 = models.TimeField(null=True, blank=True)