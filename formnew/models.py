from django.db import models


class register(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=8)
    confirm_password = models.CharField(max_length=8)
    mail_id = models.CharField(max_length=255)


class formdetails(models.Model):
    Firstname = models.CharField(max_length=10)
    Middlename = models.CharField(max_length=10)
    Lastname = models.CharField(max_length=10)
    Event = models.CharField(max_length=10)
    Available_slot = models.IntegerField()


class new_event(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    phone_no = models.IntegerField()
    event = models.CharField(max_length=255)
    time_slot = models.CharField(max_length=10)
