# Generated by Django 5.0.6 on 2024-06-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('1', 'Institute'), ('2', 'Faculty'), ('3', 'Student')], null=True),
        ),
    ]
