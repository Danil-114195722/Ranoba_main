# Generated by Django 4.1.3 on 2023-02-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_alter_book_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
    ]