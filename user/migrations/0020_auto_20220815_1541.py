# Generated by Django 3.0 on 2022-08-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20220815_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image/profile/2022-08-15-15:41:22.245332'),
        ),
    ]
