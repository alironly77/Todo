# Generated by Django 3.2.14 on 2022-08-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_remove_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
