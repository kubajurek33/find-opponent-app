# Generated by Django 3.2.14 on 2022-09-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='test',
        ),
        migrations.AddField(
            model_name='customuser',
            name='ntrp',
            field=models.FloatField(default=None),
        ),
    ]
