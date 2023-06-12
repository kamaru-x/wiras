# Generated by Django 4.2.1 on 2023-06-12 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_exam_results_exam_schedules'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_results',
            name='Date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam_results',
            name='Status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='exam_schedules',
            name='Date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam_schedules',
            name='Status',
            field=models.IntegerField(default=1),
        ),
    ]
