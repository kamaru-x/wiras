# Generated by Django 4.2.1 on 2023-06-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0016_admission_date_admission_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(max_length=25)),
                ('Batch', models.CharField(max_length=50)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='admission',
            name='Gender',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
