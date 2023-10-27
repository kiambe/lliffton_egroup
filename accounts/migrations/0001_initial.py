# Generated by Django 4.2.4 on 2023-10-27 10:41

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_member', models.BooleanField(default=False, verbose_name='Is member')),
                ('is_vendor', models.BooleanField(default=False, verbose_name='Is vendor')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
                ('code', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(blank=True, max_length=255, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('sent', models.CharField(blank=True, max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('special_code', models.CharField(blank=True, max_length=4, null=True)),
                ('group_type', models.CharField(blank=True, max_length=255, null=True)),
                ('business_activity', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_services', models.CharField(blank=True, max_length=255, null=True)),
                ('mpesa_tillnumber', models.CharField(blank=True, max_length=255, null=True)),
                ('mpesa_paybill_busines_number', models.CharField(blank=True, max_length=255, null=True)),
                ('mpesa_paybill_account_number', models.CharField(blank=True, max_length=255, null=True)),
                ('secretary_name', models.CharField(blank=True, max_length=255, null=True)),
                ('secretary_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('opportunity', models.CharField(blank=True, max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announce_at', models.DateField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('announced', models.CharField(blank=True, max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.group')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999999.9)])),
                ('amount_due', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999999.9)])),
                ('duration_days', models.IntegerField(blank=True, null=True)),
                ('penalty_rate', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99.9)])),
                ('interest', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99.9)])),
                ('interest_rate', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99.9)])),
                ('loan_type', models.CharField(blank=True, max_length=255, null=True)),
                ('borrowing_percentage', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99.9)])),
                ('borrowing_times', models.IntegerField(blank=True, null=True)),
                ('approved_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, max_length=255, null=True)),
                ('purpose', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, default='ACTIVE', max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.group')),
            ],
        ),
        migrations.CreateModel(
            name='LoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('loan_duration_days', models.IntegerField(blank=True, null=True)),
                ('penalty_rate', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99.9)])),
                ('interest_rate', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99.9)])),
                ('product_type', models.CharField(blank=True, max_length=255, null=True)),
                ('borrowing_percentage', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99.9)])),
                ('borrowing_times', models.IntegerField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('physical_address', models.TextField(blank=True, max_length=255, null=True)),
                ('national_id', models.CharField(blank=True, max_length=255, null=True)),
                ('primary_phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('primary_phone_number_provider', models.CharField(blank=True, max_length=255, null=True)),
                ('alternative_phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('alternative_phone_number_provider', models.CharField(blank=True, max_length=255, null=True)),
                ('year_of_birth', models.CharField(blank=True, max_length=4, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_img', models.ImageField(blank=True, default='default.png', null=True, upload_to='Profile')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999999.0)])),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.group')),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('lng', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('loccode', models.CharField(blank=True, max_length=255, null=True)),
                ('county_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.county')),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('expiry', models.TextField(blank=True, default=255, null=True)),
                ('amount_equivalent', models.FloatField(blank=True, default=0.0, null=True)),
                ('reviewed', models.BooleanField(blank=True, default=False, null=True)),
                ('voucher_issued', models.BooleanField(blank=True, default=False, null=True)),
                ('product_issued', models.BooleanField(blank=True, default=False, null=True)),
                ('cancelled', models.BooleanField(blank=True, default=False, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='staffadmins', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('national_id', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
                ('banned', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('lng', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('loccode', models.CharField(blank=True, max_length=255, null=True)),
                ('county_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.county')),
                ('subcounty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.subcounty')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('shopping_centre_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_person_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_person_password', models.CharField(blank=True, max_length=255, null=True)),
                ('api_key', models.CharField(blank=True, max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ward_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ward')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_training_date', models.DateField(blank=True, null=True)),
                ('completion_training_date', models.DateField(blank=True, null=True)),
                ('topic_trained', models.CharField(blank=True, max_length=255, null=True)),
                ('training_photo', models.ImageField(blank=True, null=True, upload_to='training_photos/')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
            ],
        ),
        migrations.CreateModel(
            name='SavingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999999.0)])),
                ('transaction_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('log_type', models.CharField(blank=True, max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('savings_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.saving')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('retail_price', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99999999.9)])),
                ('wholesale_price', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999999.9)])),
                ('photo', models.ImageField(blank=True, default='default.png', null=True, upload_to='Products')),
                ('description', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('vendor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999999.9)])),
                ('status', models.CharField(blank=True, default='ACTIVE', max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='ward_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ward'),
        ),
        migrations.CreateModel(
            name='LoanRepayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999999.9)])),
                ('payment_type', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_code', models.CharField(blank=True, max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('loan_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.loan')),
            ],
        ),
        migrations.CreateModel(
            name='LoanReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('send_at', models.DateTimeField(blank=True, null=True)),
                ('sent', models.CharField(blank=True, max_length=10, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.groupannouncement')),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='group_member_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.member'),
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.loanproduct'),
        ),
        migrations.AddField(
            model_name='loan',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.voucher'),
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.group')),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='ward_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ward'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('document', models.FileField(blank=True, null=True, upload_to='articles/documents/')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
