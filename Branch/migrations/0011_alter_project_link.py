# Generated by Django 4.0 on 2022-12-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0010_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=20, null=True),
        ),
    ]