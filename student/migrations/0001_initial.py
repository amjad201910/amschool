# Generated by Django 4.1.7 on 2023-03-07 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Creates', '0002_class_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=40)),
                ('LastName', models.CharField(max_length=40)),
                ('FatherName', models.CharField(max_length=40)),
                ('MotherName', models.CharField(max_length=40)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Creates.class')),
                ('Level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Creates.level')),
            ],
        ),
    ]
