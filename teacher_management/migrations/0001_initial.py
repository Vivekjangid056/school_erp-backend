# Generated by Django 4.2.13 on 2024-07-04 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institute', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LmAttendanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('nature', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')], default='Present', max_length=100)),
                ('attendance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='LmCategoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LmDepartmentMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LmDesignationMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LmHolidayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeMaster',
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
                ('reliving_reason', models.CharField(max_length=200)),
                ('reliving_date', models.DateField()),
                ('is_driver', models.BooleanField(default=False)),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=200)),
                ('office_contact', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
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
                ('drivint_license_issue_date', models.DateField()),
                ('driving_license_expiry_date', models.DateField()),
                ('driving_license_issue_palace', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200)),
                ('employee_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('signature_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_management.lmcategorymaster')),
                ('category_cast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.category')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_management.lmdepartmentmaster')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_management.lmdesignationmaster')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('nick_name', models.CharField(blank=True, max_length=50)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('confirm_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('employee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_management.employeemaster')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to='accounts.user')),
            ],
        ),
    ]
