# Generated by Django 4.0 on 2023-03-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0031_notification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Video',
            field=models.FileField(null=True, upload_to='video/%y'),
        ),
    ]
