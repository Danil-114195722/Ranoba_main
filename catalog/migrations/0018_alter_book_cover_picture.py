# Generated by Django 4.1.3 on 2023-01-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_book_cover_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_picture',
            field=models.BinaryField(),
        ),
    ]