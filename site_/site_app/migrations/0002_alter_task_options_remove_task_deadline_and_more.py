# Generated by Django 4.1.4 on 2023-01-14 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task',
        ),
    ]
