# Generated by Django 4.0.2 on 2022-04-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Klienci', '0004_klient_my_date_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='slug',
            field=models.SlugField(blank=True, default=True),
        ),
    ]