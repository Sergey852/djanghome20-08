# Generated by Django 4.1 on 2022-08-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cattleya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Cattleya name')),
                ('about', models.TextField(verbose_name='Cattleya about')),
                ('img', models.ImageField(upload_to='media', verbose_name='cattleya image')),
            ],
        ),
    ]
