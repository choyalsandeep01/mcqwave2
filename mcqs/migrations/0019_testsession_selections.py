# Generated by Django 4.2.14 on 2024-09-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0018_testanswer_correct_testanswer_selected_optiontext_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsession',
            name='selections',
            field=models.JSONField(default=list),
        ),
    ]