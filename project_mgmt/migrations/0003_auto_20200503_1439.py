# Generated by Django 3.0.5 on 2020-05-03 14:39

from django.db import migrations, models
import project_mgmt.models


class Migration(migrations.Migration):

    dependencies = [
        ('project_mgmt', '0002_auto_20200502_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterField(
            model_name='projects',
            name='avatar',
            field=models.ImageField(upload_to=project_mgmt.models.nameFile),
        ),
    ]
