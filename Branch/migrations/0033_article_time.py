# Generated by Django 4.0 on 2023-03-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0032_course_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
