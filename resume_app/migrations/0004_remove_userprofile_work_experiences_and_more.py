# Generated by Django 4.2.7 on 2024-01-14 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resume_app", "0003_workexperience_userprofile_work_experiences"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="work_experiences",),
        migrations.DeleteModel(name="WorkExperience",),
    ]
