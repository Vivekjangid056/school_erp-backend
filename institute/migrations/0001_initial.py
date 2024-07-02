<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-07-02 09:48

import colorfield.fields
import django.db.models.deletion
=======
# Generated by Django 4.2.13 on 2024-06-24 12:15

import colorfield.fields
from django.conf import settings
import django.core.validators
>>>>>>> origin/prashantdev1
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('accounts', '0001_initial'),
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> origin/prashantdev1
    ]

    operations = [
        migrations.CreateModel(
            name='Caste',
<<<<<<< HEAD
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
=======
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChildStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClassGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EnquiryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FeeHeads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_name', models.CharField(max_length=100)),
                ('tax_rate', models.IntegerField()),
                ('default_fees', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FeeInstallments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color_code', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('registration_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('institute_name', models.CharField(max_length=250)),
                ('branch_name', models.CharField(blank=True, max_length=250)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100)),
                ('billing_name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='PIN must be 6 digits.', regex='^\\d{6}$')])),
                ('mobile_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Mobile number must be 10 to 12 digits.', regex='^\\d{10,12}$')])),
                ('mobile_number2', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Mobile number must be 10 to 12 digits.', regex='^\\d{10,12}$')])),
                ('fax_number', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=100)),
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
>>>>>>> origin/prashantdev1
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChildStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClassGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EnquiryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FeeHeads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_name', models.CharField(max_length=100)),
                ('tax_rate', models.IntegerField()),
                ('default_fees', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FeeInstallments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color_code', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='LeavingReasonTC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LomSignature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature_name', models.CharField(max_length=100)),
                ('signature_heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MotherToungue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NameOfSainikSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NameOfTheBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('account_number', models.CharField(max_length=20)),
                ('account_holder_name', models.CharField(max_length=200)),
                ('branch_address', models.CharField(max_length=200)),
                ('branch_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NextClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectForClassGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentsRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_new', models.BooleanField(default=False)),
                ('for_old', models.BooleanField(default=False)),
                ('document_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.documents')),
            ],
        ),
        migrations.CreateModel(
            name='InstituteRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('branches', models.ManyToManyField(related_name='roles', to='accounts.institute')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.mainmenu')),
            ],
        ),
        migrations.CreateModel(
            name='SessionSettingsClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.nextclass')),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.standard')),
            ],
        ),
        migrations.CreateModel(
            name='ClassWiseSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compulsary', models.BooleanField(default=False)),
                ('activity', models.BooleanField(default=False)),
                ('additional', models.BooleanField(default=False)),
                ('skill', models.BooleanField(default=False)),
                ('show_in_marlsheet', models.BooleanField(default=False)),
                ('practical_fee', models.IntegerField()),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submenus', to='institute.mainmenu')),
            ],
        ),
        migrations.CreateModel(
            name='SuperSubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('submenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supersubmenus', to='institute.submenu')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_add', models.BooleanField(default=False)),
                ('can_edit', models.BooleanField(default=False)),
                ('can_view', models.BooleanField(default=False)),
                ('can_delete', models.BooleanField(default=False)),
                ('can_print', models.BooleanField(default=False)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.mainmenu')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='institute.instituterole')),
                ('submenu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.submenu')),
                ('supersubmenu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.supersubmenu')),
            ],
        ),
        migrations.AddConstraint(
            model_name='permission',
            constraint=models.UniqueConstraint(fields=('role', 'menu', 'submenu', 'supersubmenu'), name='unique_role_menu_submenu_supersubmenu'),
        ),
        migrations.CreateModel(
            name='LeavingReasonTC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LomSignature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature_name', models.CharField(max_length=100)),
                ('signature_heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MotherToungue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NameOfSainikSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NameOfTheBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('account_number', models.CharField(max_length=20)),
                ('account_holder_name', models.CharField(max_length=200)),
                ('branch_address', models.CharField(max_length=200)),
                ('branch_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NextClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectForClassGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SessionSettingsClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.standard')),
                ('next_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.nextclass')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('nick_name', models.CharField(blank=True, max_length=50)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='DocumentsRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_new', models.BooleanField(default=False)),
                ('for_old', models.BooleanField(default=False)),
                ('document_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.documents')),
            ],
        ),
        migrations.CreateModel(
            name='ClassWiseSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compulsary', models.BooleanField(default=False)),
                ('activity', models.BooleanField(default=False)),
                ('additional', models.BooleanField(default=False)),
                ('skill', models.BooleanField(default=False)),
                ('show_in_marlsheet', models.BooleanField(default=False)),
                ('practical_fee', models.IntegerField()),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.subjects')),
            ],
        ),
    ]
