# Generated by Django 3.0 on 2023-05-13 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20230513_0611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='like',
            new_name='user',
        ),
    ]
