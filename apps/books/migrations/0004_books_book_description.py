# Generated by Django 4.1.5 on 2023-02-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_books_dimensions_books_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_description',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
