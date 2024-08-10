# Generated by Django 5.0.6 on 2024-08-09 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_institutebranch_is_active"),
        ("institute", "0006_reference_session"),
    ]

    operations = [
        migrations.AddField(
            model_name="subjects",
            name="branch",
            field=models.ForeignKey(
                default="21",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subjects_branch",
                to="accounts.institutebranch",
            ),
            preserve_default=False,
        ),
    ]
