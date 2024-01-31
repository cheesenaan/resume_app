# Generated by Django 4.2.7 on 2024-01-18 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resume_app", "0013_alter_workexperience_user_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="resume_app.userprofile",
                    ),
                ),
            ],
        ),
    ]