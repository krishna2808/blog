# Generated by Django 3.0 on 2022-08-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20220815_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image/profile/2022-08-15-06:41:38.373108'),
        ),
    ]
