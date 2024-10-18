# Generated by Django 4.2.15 on 2024-10-07 10:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institute', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField(auto_created=True)),
                ('prefix', models.CharField(max_length=10)),
                ('emp_no', models.CharField(max_length=10)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], default='1')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('pan_no', models.CharField(max_length=10)),
                ('aadhar_no', models.CharField(max_length=12)),
                ('marital_status', models.CharField(choices=[('4', 'Married'), ('5', 'Single'), ('6', 'Divorced'), ('7', 'Widowed'), ('8', 'Separated')], default='5')),
                ('reliving_reason', models.CharField(blank=True, max_length=200, null=True)),
                ('reliving_date', models.DateField(blank=True, null=True)),
                ('is_driver', models.BooleanField(default=False)),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='PIN must be 6 digits.', regex='^\\d{6}$')])),
                ('mobile_number', models.CharField(max_length=200)),
                ('office_contact', models.CharField(max_length=200)),
                ('personal_email', models.EmailField(max_length=200)),
                ('roll_no_10th', models.CharField(blank=True, max_length=200, null=True)),
                ('board_year_10th', models.CharField(blank=True, max_length=200, null=True)),
                ('school_location', models.CharField(blank=True, max_length=200, null=True)),
                ('employee_status', models.CharField(choices=[('9', 'Part time'), ('10', 'Permanent'), ('11', 'Active')], default='10')),
                ('Pass_port_no', models.CharField(blank=True, max_length=200, null=True)),
                ('pass_port_end_date', models.DateField(blank=True, null=True)),
                ('punch_machine_id', models.CharField(max_length=200)),
                ('bank_account_no', models.CharField(max_length=50)),
                ('ifsc_code', models.CharField(max_length=20)),
                ('Banke_name', models.CharField(max_length=200)),
                ('branch_address', models.CharField(max_length=200)),
                ('payment_mode', models.CharField(choices=[('12', 'Cash'), ('13', 'Online'), ('14', 'Cheque'), ('15', 'DD'), ('16', 'UPI'), ('17', 'Credit Card'), ('18', 'Debit Card')], default='12')),
                ('qualification', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
                ('experience_detail', models.CharField(max_length=200)),
                ('uan_no', models.CharField(max_length=200)),
                ('pf_no', models.CharField(max_length=200)),
                ('esi_no', models.CharField(max_length=200)),
                ('apply_maximum_pf_limit', models.BooleanField(default=False)),
                ('driving_license_no', models.CharField(max_length=200)),
                ('driving_license_issue_date', models.DateField()),
                ('driving_license_expiry_date', models.DateField()),
                ('driving_license_issue_palace', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200)),
                ('employee_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('signature_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_branch', to='accounts.institutebranch')),
            ],
        ),
        migrations.CreateModel(
            name='LmHolidayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lm_holiday_list_branch', to='accounts.institutebranch')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lmholiday', to='accounts.institute')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lm_holiday_list_session', to='accounts.academicsession')),
            ],
        ),
        migrations.CreateModel(
            name='LmDesignationMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lm_designation_branch', to='accounts.institutebranch')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lmdesignation', to='accounts.institute')),
            ],
        ),
        migrations.CreateModel(
            name='LmDepartmentMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lm_department_branch', to='accounts.institutebranch')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lmdepartment', to='accounts.institute')),
            ],
        ),
        migrations.CreateModel(
            name='LmCategoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lm_category_branch', to='accounts.institutebranch')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lmcategory', to='accounts.institute')),
            ],
        ),
        migrations.CreateModel(
            name='LmAttendanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('nature', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')], default='Present', max_length=100)),
                ('attendance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lm_attendance_type_branch', to='accounts.institutebranch')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lm_attendace_type', to='accounts.institute')),
            ],
        ),
        migrations.CreateModel(
            name='LiveClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_date', models.DateField(blank=True, null=True)),
                ('class_time', models.TimeField(blank=True, null=True)),
                ('chapter', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_class_branch', to='accounts.institutebranch')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_class_employee', to='teacher_management.employee')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_class_institute', to='accounts.institute')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_class_section', to='institute.section')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_class_session', to='accounts.academicsession')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_class_standard', to='institute.standard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_class_subjects', to='institute.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField(default=False)),
                ('absent', models.BooleanField(default=False)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_attendance_branch', to='accounts.institutebranch')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_management.employee')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_attendance_session', to='accounts.academicsession')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_category', to='teacher_management.lmcategorymaster'),
        ),
        migrations.AddField(
            model_name='employee',
            name='category_cast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_category_cast', to='institute.category'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_department', to='teacher_management.lmdepartmentmaster'),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_category', to='teacher_management.lmdesignationmaster'),
        ),
        migrations.AddField(
            model_name='employee',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_institute', to='accounts.institute'),
        ),
        migrations.AddField(
            model_name='employee',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_session', to='accounts.academicsession'),
        ),
        migrations.AddField(
            model_name='employee',
            name='staff_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_staff_role', to='institute.instituterole'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('submission_date', models.DateField(blank=True, null=True)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('attachment', models.FileField(upload_to='documents/')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_branch', to='accounts.institutebranch')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_employee', to='teacher_management.employee')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_institute', to='accounts.institute')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_section', to='institute.section')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_session', to='accounts.academicsession')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_standard', to='institute.standard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_subjects', to='institute.subjects')),
            ],
        ),
    ]
