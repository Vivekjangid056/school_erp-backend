# Generated by Django 4.2.13 on 2024-07-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees_module', '0006_alter_paymentschedule_due_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentfeepayment',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
