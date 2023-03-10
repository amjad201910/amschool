# Generated by Django 4.1.7 on 2023-03-09 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Creates', '0005_delete_notification'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSchedul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_on', models.DateField()),
                ('From', models.TimeField()),
                ('To', models.TimeField()),
                ('Day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subject.day')),
                ('Level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creates.level')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject')),
            ],
        ),
    ]
