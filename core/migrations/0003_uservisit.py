# Generated by Django 5.0.3 on 2025-01-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_project_github_link_alter_project_website_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
