# Generated by Django 2.1 on 2020-03-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('DOB', models.DateTimeField()),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
