# Generated by Django 4.0 on 2023-03-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0024_alter_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
