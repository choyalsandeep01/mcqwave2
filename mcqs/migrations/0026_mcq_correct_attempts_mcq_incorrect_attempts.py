# Generated by Django 4.2.14 on 2024-12-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0025_testsession_totaltime'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='correct_attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mcq',
            name='incorrect_attempts',
            field=models.IntegerField(default=0),
        ),
    ]