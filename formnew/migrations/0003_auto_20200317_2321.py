# Generated by Django 2.1 on 2020-03-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formnew', '0002_formdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='confirm_password',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='mail_id',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
