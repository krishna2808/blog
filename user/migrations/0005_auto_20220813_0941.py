# Generated by Django 3.0 on 2022-08-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220813_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/profile/2022-08-13-09:41:33.442188'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
