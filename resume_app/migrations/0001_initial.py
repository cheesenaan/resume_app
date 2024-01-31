# Generated by Django 4.2.7 on 2024-01-05 11:45

from django.db import migrations, models
import resume_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="test",
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
                ("NAME", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="user_resume_data",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("NAME", models.CharField(max_length=100, null=True)),
                ("LINK", models.CharField(max_length=100, null=True)),
                ("EMAIL", models.EmailField(max_length=254, null=True)),
                ("PHONE", models.CharField(max_length=20, null=True)),
                ("CITY", models.CharField(max_length=100, null=True)),
                ("STATE", models.CharField(max_length=50, null=True)),
                ("RESUME_LINK", models.URLField(null=True)),
                ("UNIVERSITY", models.CharField(max_length=100, null=True)),
                ("DEGREE_TYPE", models.CharField(max_length=100, null=True)),
                ("UNIVERSITY_START_DATE", models.CharField(max_length=100, null=True)),
                ("UNIVERSITY_END_DATE", models.CharField(max_length=100, null=True)),
                ("MAJOR", models.CharField(max_length=100, null=True)),
                ("MINOR", models.CharField(max_length=100, null=True)),
                ("GPA", models.FloatField(null=True)),
                ("EXPERIENCE1", models.CharField(max_length=200, null=True)),
                ("EXPERIENCE1_START_DATE", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE1_END_DATE", models.CharField(max_length=100, null=True)),
                ("TITLE1", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE1_LOCATION", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE1_BULLET1", models.TextField(null=True)),
                ("EXPERIENCE1_BULLET2", models.TextField(null=True)),
                ("EXPERIENCE1_BULLET3", models.TextField(null=True)),
                ("EXPERIENCE2", models.CharField(max_length=200, null=True)),
                ("EXPERIENCE2_START_DATE", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE2_END_DATE", models.CharField(max_length=100, null=True)),
                ("TITLE2", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE2_LOCATION", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE2_BULLET1", models.TextField(null=True)),
                ("EXPERIENCE2_BULLET2", models.TextField(null=True)),
                ("EXPERIENCE2_BULLET3", models.TextField(null=True)),
                ("EXPERIENCE3", models.CharField(max_length=200, null=True)),
                ("EXPERIENCE3_START_DATE", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE3_END_DATE", models.CharField(max_length=100, null=True)),
                ("TITLE3", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE3_LOCATION", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE3_BULLET1", models.TextField(null=True)),
                ("EXPERIENCE3_BULLET2", models.TextField(null=True)),
                ("EXPERIENCE3_BULLET3", models.TextField(null=True)),
                ("EXPERIENCE4", models.CharField(max_length=200, null=True)),
                ("EXPERIENCE4_START_DATE", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE4_END_DATE", models.CharField(max_length=100, null=True)),
                ("TITLE4", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE4_LOCATION", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE4_BULLET1", models.TextField(null=True)),
                ("EXPERIENCE4_BULLET2", models.TextField(null=True)),
                ("EXPERIENCE4_BULLET3", models.TextField(null=True)),
                ("EXPERIENCE5", models.CharField(max_length=200, null=True)),
                ("EXPERIENCE5_START_DATE", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE5_END_DATE", models.CharField(max_length=100, null=True)),
                ("TITLE5", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE5_LOCATION", models.CharField(max_length=100, null=True)),
                ("EXPERIENCE5_BULLET1", models.TextField(null=True)),
                ("EXPERIENCE5_BULLET2", models.TextField(null=True)),
                ("EXPERIENCE5_BULLET3", models.TextField(null=True)),
                ("PROJECT1", models.CharField(max_length=100, null=True)),
                ("PROJECT1_BULLET1", models.TextField(null=True)),
                ("PROJECT1_BULLET2", models.TextField(null=True)),
                ("PROJECT2", models.CharField(max_length=100, null=True)),
                ("PROJECT2_BULLET1", models.TextField(null=True)),
                ("PROJECT2_BULLET2", models.TextField(null=True)),
                ("PROJECT3", models.CharField(max_length=100, null=True)),
                ("PROJECT3_BULLET1", models.TextField(null=True)),
                ("PROJECT3_BULLET2", models.TextField(null=True)),
                ("PROJECT4", models.CharField(max_length=100, null=True)),
                ("PROJECT4_BULLET1", models.TextField(null=True)),
                ("PROJECT4_BULLET2", models.TextField(null=True)),
                ("PROJECT5", models.CharField(max_length=100, null=True)),
                ("PROJECT5_BULLET1", models.TextField(null=True)),
                ("PROJECT5_BULLET2", models.TextField(null=True)),
                ("LANGUAGES", models.CharField(max_length=200, null=True)),
                ("TECHNOLOGIES", models.CharField(max_length=200, null=True)),
                ("LEADERSHIP", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "url_name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        validators=[resume_app.models.validate_unique_url_name],
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("city", models.CharField(max_length=255)),
                ("state", models.CharField(max_length=255)),
                ("link", models.URLField()),
                ("profile_image", models.ImageField(upload_to="")),
            ],
        ),
    ]
