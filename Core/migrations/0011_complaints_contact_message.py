# Generated by Django 4.2.1 on 2023-06-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0010_album_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=225)),
                ('Last_Name', models.CharField(max_length=225, null=True)),
                ('Student_Id', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Department', models.CharField(max_length=225, null=True)),
                ('Batch', models.CharField(max_length=225)),
                ('Complaint', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=225)),
                ('Phone', models.CharField(max_length=25)),
                ('Description', models.TextField()),
                ('Information', models.CharField(max_length=225)),
            ],
        ),
    ]
