# Generated by Django 4.0 on 2022-12-06 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0013_rename_link_project_link_project_github'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link_project_github',
        ),
    ]