# Generated by Django 4.0.2 on 2022-06-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_alter_profile_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='companycode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
