# Generated by Django 3.0.5 on 2020-05-02 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='accepted_by',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
    ]