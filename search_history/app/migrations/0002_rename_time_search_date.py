# Generated by Django 3.2.6 on 2021-09-01 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='time',
            new_name='date',
        ),
    ]