# Generated by Django 3.0 on 2022-08-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('user_about', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/profile/2022-08-13-09:35:58.577831')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
