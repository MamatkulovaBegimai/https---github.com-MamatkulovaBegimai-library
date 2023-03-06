# Generated by Django 4.1.5 on 2023-01-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Настройка', 'verbose_name_plural': 'Настройки'},
        ),
        migrations.AddField(
            model_name='settings',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='graphic',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='phone',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='street',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.FileField(upload_to='logo/'),
        ),
    ]
