# Generated by Django 5.0.6 on 2024-07-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_management', '0005_alter_employeemaster_emp_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='last_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
