# Generated by Django 2.1 on 2020-03-17 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formnew', '0003_auto_20200317_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='DOB',
        ),
    ]
