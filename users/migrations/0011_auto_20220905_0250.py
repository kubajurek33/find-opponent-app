# Generated by Django 3.2.14 on 2022-09-05 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_customuser_ntrp2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ntrp',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='ntrp2',
        ),
    ]
