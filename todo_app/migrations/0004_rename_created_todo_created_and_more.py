# Generated by Django 4.0.6 on 2022-08-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todo_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='created',
            new_name='Created',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='body',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='Title',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
        migrations.AddField(
            model_name='todo',
            name='Status',
            field=models.CharField(choices=[('do', 'Doing'), ('f', 'Finished'), ('s', 'Started')], default='do', max_length=2),
        ),
    ]
