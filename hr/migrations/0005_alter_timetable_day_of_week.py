# Generated by Django 4.2.13 on 2024-07-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_alter_timetable_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day_of_week',
            field=models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=10),
        ),
    ]
