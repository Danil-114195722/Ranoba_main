# Generated by Django 4.1.3 on 2023-01-31 17:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_book_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
