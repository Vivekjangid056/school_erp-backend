# Generated by Django 5.0.6 on 2024-07-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teacher_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employeemaster",
            name="pin",
            field=models.CharField(max_length=6),
        ),
    ]
