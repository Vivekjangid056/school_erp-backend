# Generated by Django 4.2.13 on 2024-07-10 11:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=100)),
                ('form_no', models.BigIntegerField()),
                ('date_of_admission', models.DateField()),
                ('registration_date', models.DateField()),
                ('stream', models.CharField(blank=True, choices=[('science', 'Science'), ('commerce', 'Commerce'), ('maths', 'Maths'), ('arts', 'Arts')], max_length=100)),
                ('date_of_deactivae', models.DateField(blank=True)),
                ('rte', models.BooleanField(default=False)),
                ('bpl', models.BooleanField(default=False)),
                ('prefix', models.CharField(max_length=100)),
                ('suffix', models.CharField(max_length=100)),
                ('sr_no', models.CharField(max_length=100)),
                ('reg_no', models.CharField(max_length=255)),
                ('admission_no', models.BigIntegerField()),
                ('enroll_no', models.BigIntegerField()),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')])),
                ('dob', models.DateField()),
                ('student_aadhar', models.CharField(blank=True, max_length=100)),
                ('rural_or_urban', models.CharField(choices=[('rural', 'Rural'), ('urban', 'Urban')])),
                ('disablity_type', models.CharField(choices=[('NOT APPLICABLE', 'NOT APPLICABLE'), ('BLINDNESS', 'BLINDNESS'), ('LOW VISION', 'LOW VISION'), ('HEARING', 'HEARING'), ('AUTISM', 'AUTISM'), ('MENTAL RETARDNESS', 'MENTAL RETARDNESS'), ('LEARNING DISABLITY', 'LEARNING DISABLITY'), ('CEREBRAL PALSY', 'CEREBRAL PALSY'), ('MULTIPLE DISABLITIES', 'MULTIPLE DISABLITIESY'), ('SPEECH', 'SPEECH')])),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB- ', ' AB-'), ('O+ ', ' O+'), ('O- ', ' O-')])),
                ('place_of_birth', models.CharField(blank=True, max_length=255)),
                ('staff_refrence', models.CharField(blank=True, max_length=255)),
                ('admission_confirm_date', models.DateField(blank=True)),
                ('board_type', models.CharField(max_length=255)),
                ('fathers_name', models.CharField(max_length=255)),
                ('fathers_occupation', models.CharField(blank=True, max_length=255)),
                ('fathers_mob_no', models.CharField(max_length=255)),
                ('fathers_email', models.CharField(blank=True, max_length=255)),
                ('mothers_name', models.CharField(max_length=255)),
                ('mothers_occupation', models.CharField(blank=True, max_length=255)),
                ('mothers_mob_no', models.CharField(blank=True, max_length=255)),
                ('mothers_email', models.CharField(blank=True, max_length=255)),
                ('fahers_aadhar_no', models.CharField(blank=True, max_length=255)),
                ('mothers_aadhar_no', models.CharField(blank=True, max_length=255)),
                ('father_annual_income', models.CharField(blank=True, max_length=255)),
                ('mother_annual_income', models.CharField(blank=True, max_length=255)),
                ('father_qualification', models.CharField(blank=True, max_length=255)),
                ('mother_qualification', models.CharField(blank=True, max_length=255)),
                ('father_pan_no', models.CharField(blank=True, max_length=255)),
                ('mother_pan_no', models.CharField(blank=True, max_length=255)),
                ('guardian_name', models.CharField(blank=True, max_length=255)),
                ('guardian_mobile', models.CharField(blank=True, max_length=255)),
                ('guardian_relation', models.CharField(blank=True, max_length=255)),
                ('fee_deposited_by', models.CharField(blank=True, max_length=255)),
                ('sms_mob_no', models.CharField(blank=True, max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('pin', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='PIN must be 6 digits.', regex='^\\d{6}$')])),
                ('previous_school_name', models.CharField(blank=True, max_length=255)),
                ('previous_school_address', models.CharField(blank=True, max_length=255)),
                ('reason_of_leaving', models.CharField(blank=True, max_length=255)),
                ('previous_year', models.CharField(blank=True, max_length=255)),
                ('previous_class', models.CharField(blank=True, max_length=255)),
                ('obtain_marks', models.IntegerField(blank=True)),
                ('maximum_marks', models.IntegerField(blank=True)),
                ('percentage', models.FloatField(blank=True)),
                ('result', models.CharField(blank=True, max_length=10)),
                ('previous_school_board', models.CharField(blank=True, max_length=100)),
                ('previous_school_rollNo', models.CharField(blank=True, max_length=100)),
                ('previous_school_class', models.CharField(blank=True, max_length=100)),
                ('third_lang_studied', models.CharField(blank=True, max_length=100)),
                ('student_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('fathers_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('mothers_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('guardians_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('caution_money_reciept_no', models.CharField(blank=True, max_length=255)),
                ('caution_money_reciept_date', models.CharField(blank=True, max_length=255)),
                ('amount', models.IntegerField()),
                ('counsellor_name', models.CharField(max_length=255)),
                ('remark', models.CharField(blank=True, max_length=255)),
                ('caste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.caste')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.category')),
                ('child_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.childstatus')),
                ('discount_scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.discountscheme')),
                ('house_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.house')),
                ('installment_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.feeinstallments')),
                ('medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.medium')),
                ('mother_tongue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.mothertoungue')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.nationality')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.religion')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.section')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.standard')),
                ('student_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.studenttype')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
