# Generated by Django 5.0.6 on 2024-08-07 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_academicsession_name"),
        (
            "fees_module",
            "0003_alter_feestructure_branch_alter_feestructure_session_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="feestructure",
            name="institute",
            field=models.ForeignKey(
                default="719",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fee_structure_institute",
                to="accounts.institute",
            ),
            preserve_default=False,
        ),
    ]
