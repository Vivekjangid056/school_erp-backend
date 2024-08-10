# Generated by Django 5.0.6 on 2024-08-07 07:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("institute", "0001_initial"),
        ("teacher_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HrInterview",
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
                ("interview_no", models.IntegerField()),
                ("interview_date", models.DateField()),
                ("first_name", models.CharField(max_length=30)),
                ("middle_name", models.CharField(blank=True, max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                (
                    "gender",
                    models.CharField(
                        choices=[("1", "Male"), ("2", "Female"), ("3", "Other")]
                    ),
                ),
                ("father_name", models.CharField(max_length=20)),
                ("mother_name", models.CharField(max_length=20)),
                ("date_of_birth", models.DateField()),
                ("current_salary", models.IntegerField()),
                ("expected_salary", models.IntegerField()),
                (
                    "marital_status",
                    models.CharField(
                        choices=[
                            ("4", "Married"),
                            ("5", "Single"),
                            ("7", "Widowed"),
                            ("8", "Separated"),
                        ]
                    ),
                ),
                (
                    "user_image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("current_address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=40)),
                (
                    "pin",
                    models.CharField(
                        max_length=6,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="PIN must be 6 digits.", regex="^\\d{6}$"
                            )
                        ],
                    ),
                ),
                ("mobile", models.CharField(max_length=12)),
                ("mobile2", models.CharField(blank=True, max_length=12)),
                ("email", models.EmailField(max_length=254)),
                ("company_name", models.CharField(max_length=255)),
                ("prev_comp_hr_no", models.CharField(max_length=20)),
                ("work_profile", models.CharField(max_length=255)),
                ("joining_date", models.DateField()),
                ("leaving_date", models.DateField(max_length=255)),
                ("leaving_reason", models.CharField(max_length=255)),
                ("salary", models.IntegerField()),
                ("recommendation_positive", models.BooleanField(default=False)),
                ("recommendation_negative", models.BooleanField(default=False)),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "1"),
                            (2, "2"),
                            (3, "3"),
                            (4, "4"),
                            (5, "5"),
                            (6, "6"),
                            (7, "7"),
                            (8, "8"),
                            (9, "9"),
                            (10, "10"),
                        ]
                    ),
                ),
                (
                    "select_for_next_round",
                    models.CharField(choices=[("9", "YES"), ("10", "NO")]),
                ),
                ("date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[("11", "PROCESS"), ("12", "SELECT"), ("13", "REJECT")]
                    ),
                ),
                ("overall_comment", models.CharField(max_length=255)),
                ("remark", models.CharField(max_length=100)),
                (
                    "assign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_interviews_assign",
                        to="teacher_management.employee",
                    ),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_interivew",
                        to="accounts.institutebranch",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="institute.category",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="teacher_management.lmdepartmentmaster",
                    ),
                ),
                (
                    "designation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="teacher_management.lmdesignationmaster",
                    ),
                ),
                (
                    "institute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interview",
                        to="accounts.institute",
                    ),
                ),
                (
                    "reference",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_interviews_reference",
                        to="teacher_management.employee",
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_interview",
                        to="accounts.academicsession",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TimeTable",
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
                    "day_of_week",
                    models.CharField(
                        choices=[
                            ("MON", "Monday"),
                            ("TUE", "Tuesday"),
                            ("WED", "Wednesday"),
                            ("THU", "Thursday"),
                            ("FRI", "Friday"),
                            ("SAT", "Saturday"),
                            ("SUN", "Sunday"),
                        ],
                        max_length=10,
                    ),
                ),
                ("period_no", models.IntegerField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timetable",
                        to="teacher_management.employee",
                    ),
                ),
                (
                    "institute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timetable",
                        to="accounts.institute",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timetable",
                        to="institute.section",
                    ),
                ),
                (
                    "standard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timetable",
                        to="institute.standard",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timetable",
                        to="institute.subjects",
                    ),
                ),
            ],
        ),
    ]
