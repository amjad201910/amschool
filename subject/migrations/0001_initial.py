# Generated by Django 4.1.7 on 2023-03-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('Name', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('Name', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
