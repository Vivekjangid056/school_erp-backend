# Generated by Django 4.2.13 on 2024-08-01 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0002_chatmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectsforclassgroup',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.subjects'),
        ),
    ]
