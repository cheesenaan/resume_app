# Generated by Django 4.2.7 on 2024-01-17 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resume_app", "0011_remove_workexperience_user_profiles_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workexperience",
            name="user_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="resume_app.userprofile"
            ),
        ),
    ]
