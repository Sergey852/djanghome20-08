# Generated by Django 4.1 on 2022-08-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_chiloschista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Vanda name')),
                ('about', models.TextField(verbose_name='Vanda about')),
                ('img', models.ImageField(upload_to='media', verbose_name='Vanda image')),
            ],
        ),
    ]