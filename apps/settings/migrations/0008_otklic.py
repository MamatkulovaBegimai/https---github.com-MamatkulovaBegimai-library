# Generated by Django 4.1.5 on 2023-02-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_rename_employee_name_team_worker_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otklic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=55)),
                ('phone', models.CharField(max_length=22)),
                ('subject', models.CharField(max_length=222)),
                ('text', models.TextField(max_length=3333)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
    ]
