# Generated by Django 4.1.5 on 2023-01-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_photo',
            field=models.ImageField(default=1, upload_to='books_photo/'),
            preserve_default=False,
        ),
    ]
