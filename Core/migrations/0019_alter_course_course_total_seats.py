# Generated by Django 4.2.1 on 2023-06-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0018_alumni_registration_status_news_letter_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Course_Total_Seats',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
