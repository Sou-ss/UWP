# Generated by Django 4.0.2 on 2022-03-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Klienci', '0003_klient_timestamp_klient_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='my_date_field',
            field=models.DateTimeField(null=True),
        ),
    ]
