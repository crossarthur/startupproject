# Generated by Django 4.2.4 on 2023-09-01 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupapp', '0002_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_duration',
            field=models.IntegerField(default=0),
        ),
    ]