# Generated by Django 4.2.7 on 2024-01-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume_app", "0005_workexperience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="url_name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
