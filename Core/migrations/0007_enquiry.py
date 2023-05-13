# Generated by Django 4.2.1 on 2023-05-13 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(max_length=225)),
                ('DOB', models.DateField()),
                ('Qualification', models.CharField(max_length=225)),
                ('Mobile_Number', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=225, null=True)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Core.course')),
            ],
        ),
    ]
