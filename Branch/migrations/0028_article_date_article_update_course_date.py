# Generated by Django 4.0 on 2023-03-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0027_alter_notification_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Date',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='update',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='Date',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
