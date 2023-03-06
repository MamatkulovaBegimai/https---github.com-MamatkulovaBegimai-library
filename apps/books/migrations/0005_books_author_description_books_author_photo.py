# Generated by Django 4.1.5 on 2023-02-05 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_authors_about_author'),
        ('books', '0004_books_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author_description',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='author_description', to='authors.authors'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='author_photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='author_photo', to='authors.authors'),
            preserve_default=False,
        ),
    ]