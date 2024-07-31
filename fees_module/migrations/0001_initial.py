# Generated by Django 5.0.6 on 2024-07-31 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("institute", "0001_initial"),
        ("scholar_register", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeeStructure",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_fee", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "institute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fee_structure",
                        to="accounts.institute",
                    ),
                ),
                (
                    "standard",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="institute.standard",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentFeePayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "installment_frequency",
                    models.CharField(
                        choices=[
                            ("Half-Yearly", "Half-Yearly"),
                            ("Monthly", "Monthly"),
                            ("No Installement", "No Installement"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "fee_structure",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fees_module.feestructure",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scholar_register.studentprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PaymentSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount_paid", models.IntegerField()),
                ("due_amount", models.IntegerField(blank=True, null=True)),
                ("payment_date", models.DateField()),
                ("payment_due_date", models.DateField(blank=True, null=True)),
                (
                    "student_fee_payment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to="fees_module.studentfeepayment",
                    ),
                ),
            ],
        ),
    ]
