# Generated by Django 4.0 on 2023-03-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0023_course_notification_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
