# Generated by Django 4.1.3 on 2022-12-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.BinaryField(max_length=100, unique=True)),
                ('salt', models.BinaryField(max_length=100)),
            ],
        ),
    ]