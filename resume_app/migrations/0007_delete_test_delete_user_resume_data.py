# Generated by Django 4.2.7 on 2024-01-17 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resume_app", "0006_alter_userprofile_url_name"),
    ]

    operations = [
        migrations.DeleteModel(name="test",),
        migrations.DeleteModel(name="user_resume_data",),
    ]
