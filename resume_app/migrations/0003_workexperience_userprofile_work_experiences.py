# Generated by Django 4.2.7 on 2024-01-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resume_app", "0002_userprofile_end_date_userprofile_institution_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkExperience",
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
                ("company_name", models.CharField(max_length=255)),
                ("job_title", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("job_description", models.TextField()),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resume_app.userprofile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="userprofile",
            name="work_experiences",
            field=models.ManyToManyField(blank=True, to="resume_app.workexperience"),
        ),
    ]
