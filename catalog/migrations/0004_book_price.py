# Generated by Django 5.1.6 on 2025-02-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_book_author_alter_book_categories_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="price",
            field=models.IntegerField(default=10000),
            preserve_default=False,
        ),
    ]
