# Generated by Django 4.2.1 on 2023-06-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_course_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='Cover_Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]