# Generated by Django 5.0.3 on 2024-03-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="contact",
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
                ("full_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=200, null=True)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="project",
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
                ("title", models.CharField(max_length=300)),
                ("description", models.TextField()),
                ("image", models.ImageField(null=True, upload_to="project")),
                ("github_link", models.URLField(null=True)),
                ("website_link", models.URLField(null=True)),
            ],
        ),
    ]
