# Generated by Django 4.2.14 on 2024-08-19 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0009_alter_unit_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcq',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='mcq',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='mcq',
            name='unit',
        ),
        migrations.AddField(
            model_name='mcq',
            name='bulk_input',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='mcqs.topic'),
        ),
    ]
