# Generated by Django 4.2.6 on 2023-10-24 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='time_stamp',
            new_name='timestamp',
        ),
    ]
