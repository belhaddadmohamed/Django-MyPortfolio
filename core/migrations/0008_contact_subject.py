# Generated by Django 5.0.3 on 2025-03-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_contact_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='No Subject', max_length=200),
        ),
    ]
