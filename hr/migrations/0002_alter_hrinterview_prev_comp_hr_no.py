# Generated by Django 4.2.13 on 2024-07-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrinterview',
            name='prev_comp_hr_no',
            field=models.CharField(max_length=20),
        ),
    ]
