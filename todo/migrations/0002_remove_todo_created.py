# Generated by Django 4.2.1 on 2023-05-16 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created',
        ),
    ]
