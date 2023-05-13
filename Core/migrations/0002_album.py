# Generated by Django 4.2.1 on 2023-05-13 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Added_Date', models.DateTimeField(auto_now_add=True)),
                ('Status', models.IntegerField(default=1)),
                ('Ip', models.GenericIPAddressField(null=True)),
                ('Edited_Date', models.DateField(null=True)),
                ('Edited_Ip', models.GenericIPAddressField(null=True)),
                ('Album_Category', models.CharField(max_length=225)),
                ('Album_Title', models.CharField(max_length=225)),
                ('Seo_Url', models.CharField(max_length=500, null=True)),
                ('Seo_Title', models.CharField(max_length=225, null=True)),
                ('Seo_Keywords', models.CharField(max_length=500, null=True)),
                ('Seo_Description', models.TextField(null=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='AddedBy', to=settings.AUTH_USER_MODEL)),
                ('EditedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
