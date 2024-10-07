# Generated by Django 4.2.15 on 2024-08-14 06:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('1', 'Super_admin'), ('2', 'Institute_Owner'), ('3', 'Management_Employee'), ('4', 'Employee'), ('5', 'Student')], max_length=2)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('country_code', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user can belong to multiple groups. A group grants access to a set of permissions.', related_name='user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_permissions', to='auth.permission', verbose_name='user permissions')),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('1', 'Super_admin'), ('2', 'Institute_Owner'), ('3', 'Management_Employee'), ('4', 'Employee'), ('5', 'Student')], max_length=2)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('country_code', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user can belong to multiple groups. A group grants access to a set of permissions.', related_name='user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('registration_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('institute_name', models.CharField(max_length=250)),
                ('number_of_branches', models.CharField(blank=True, max_length=250)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100)),
                ('billing_name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='PIN must be 6 digits.', regex='^\\d{6}$')])),
                ('mobile_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Mobile number must be 10 to 12 digits.', regex='^\\d{10,12}$')])),
                ('mobile_number2', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Mobile number must be 10 to 12 digits.', regex='^\\d{10,12}$')])),
                ('fax_number', models.CharField(blank=True, max_length=100)),
                ('institute_email', models.EmailField(max_length=100)),
                ('website', models.CharField(blank=True, max_length=255)),
                ('principal_name', models.CharField(blank=True, max_length=100)),
                ('acc_start_year', models.CharField(max_length=100)),
                ('session_start_month', models.CharField(max_length=15)),
                ('accredited_by', models.CharField(max_length=20)),
                ('scholar_prefix', models.CharField(blank=True, max_length=50)),
                ('scholar_suffix', models.CharField(blank=True, max_length=50)),
                ('emp_no_prefix', models.CharField(blank=True, max_length=100)),
                ('no_of_pg_in_tcbook', models.CharField(blank=True, max_length=255)),
                ('auto_enroll_no', models.BooleanField(default=False)),
                ('std_attd_assignment', models.BooleanField(default=False)),
                ('live_class_show_time', models.BooleanField(default=False)),
                ('allow_edit_emp_attd_time', models.BooleanField(default=False)),
                ('show_std_contact_no_app', models.BooleanField(default=False)),
                ('change_zoom_url', models.BooleanField(default=False)),
                ('auto_admin_number', models.BooleanField(default=False)),
                ('live_class_log_Std', models.BooleanField(default=False)),
                ('suggest_auto_section', models.BooleanField(default=False)),
                ('send_Std_wc_msg', models.BooleanField(default=False)),
                ('auto_scholar_no', models.BooleanField(default=False)),
                ('single_login', models.BooleanField(default=False)),
                ('suggest_auto_house', models.BooleanField(default=False)),
                ('allow_ss_in_app', models.BooleanField(default=True)),
                ('auto_emp_no', models.BooleanField(default=False)),
                ('std_attd_through_live_class', models.BooleanField(default=False)),
                ('login_with_single_device', models.BooleanField(default=False)),
                ('show_yt_opt_4_app', models.BooleanField(default=False)),
                ('show_teach_mo_no_app', models.BooleanField(default=False)),
                ('show_exam_list_res_wise', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institute_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InstituteBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='accounts.institute')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the academic session', max_length=100)),
                ('session_start_month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], help_text='Month when the academic session starts', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('session_duration', models.IntegerField(choices=[(1, '1 month'), (2, '2 months'), (3, '3 months'), (4, '4 months'), (5, '5 months'), (6, '6 months'), (7, '7 months'), (8, '8 months'), (9, '9 months'), (10, '10 months'), (11, '11 months'), (12, '12 months')], default=6, help_text='Duration of the academic session in months')),
                ('start_date', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='accounts.institute')),
            ],
            options={
                'verbose_name': 'Academic Session',
                'verbose_name_plural': 'Academic Sessions',
                'ordering': ['-start_date'],
            },
        ),
    ]
