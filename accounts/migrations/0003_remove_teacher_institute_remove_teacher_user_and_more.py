# Generated by Django 5.0.6 on 2024-06-16 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_institute_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='institute',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
