# Generated by Django 4.1 on 2022-08-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('is_superuser', models.BooleanField(db_index=True, default=False, verbose_name='Is Superuser')),
                ('is_staff', models.BooleanField(db_index=True, default=False, verbose_name='Is Staff')),
                ('first_name', models.CharField(blank=True, default='', max_length=64, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, default='', max_length=64, verbose_name='Last Name')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='Address')),
                ('phone_number', models.CharField(blank=True, default='', max_length=20, verbose_name='Phone Number')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date Of Birth')),
                ('postcode', models.CharField(blank=True, max_length=32, verbose_name='Postcode')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='', max_length=11, verbose_name='Gender')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'ordering': ['-modified'],
            },
        ),
    ]
