# Generated by Django 2.2.3 on 2019-07-09 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone_numer',
            new_name='phone_number',
        ),
    ]
