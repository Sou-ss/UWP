# Generated by Django 4.0.2 on 2022-03-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Klienci', '0002_klient_comments_klient_dogs_name_klient_dogs_race_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='klient',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
