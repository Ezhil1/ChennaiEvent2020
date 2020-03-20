# Generated by Django 2.1 on 2020-03-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formnew', '0007_auto_20200318_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=255)),
                ('phone_no', models.IntegerField()),
                ('event', models.CharField(max_length=255)),
                ('time_slot', models.CharField(max_length=10)),
            ],
        ),
    ]