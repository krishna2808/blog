# Generated by Django 3.0 on 2023-05-13 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20230506_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='image/profile/2023-05-13-05:02:11.713543'),
        ),
    ]
