# Generated by Django 4.1.3 on 2023-01-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_book_cover_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(upload_to='Ranoba_main/Books/<django.db.models.fields.CharField>/cover_picture/cover_picture.jpg'),
        ),
    ]
