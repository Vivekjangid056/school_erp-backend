# Generated by Django 4.2.13 on 2024-07-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='admission_confirm_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='caution_money_reciept_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='date_of_deactivae',
            field=models.DateField(blank=True, null=True),
        ),
    ]
