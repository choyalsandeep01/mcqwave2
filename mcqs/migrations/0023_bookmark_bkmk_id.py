# Generated by Django 4.2.14 on 2024-09-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0022_alter_bookmark_bookmark_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='bkmk_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]