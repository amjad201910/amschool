# Generated by Django 4.1.7 on 2023-03-09 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Creates', '0004_remove_notification_id_alter_notification_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
