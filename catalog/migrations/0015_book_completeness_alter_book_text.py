# Generated by Django 4.1.3 on 2023-01-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_book_chapters'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='completeness',
            field=models.CharField(choices=[('Завершено', 'Завершено'), ('Не завершено', 'Не завершено')], default='Не завершено', max_length=12),
        ),
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.CharField(max_length=150),
        ),
    ]
