# Generated by Django 5.1.6 on 2025-02-19 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_rename_auth_book_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ManyToManyField(related_name="books", to="catalog.author"),
        ),
        migrations.AlterField(
            model_name="book",
            name="categories",
            field=models.ManyToManyField(
                related_name="books",
                through="catalog.BookCategory",
                to="catalog.category",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="books",
                to="catalog.publisher",
            ),
        ),
    ]
