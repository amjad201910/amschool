# Generated by Django 4.1.7 on 2023-03-09 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0004_remove_examschedul_level_alter_examschedul_from_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examschedul',
            old_name='Created_on',
            new_name='Date',
        ),
    ]
