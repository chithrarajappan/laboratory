# Generated by Django 2.2.4 on 2019-11-04 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addtestresult',
            name='Technician_Name',
        ),
    ]
