# Generated by Django 2.1 on 2020-03-22 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formnew', '0008_new_event'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='enroll',
        ),
    ]
