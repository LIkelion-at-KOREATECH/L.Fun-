# Generated by Django 2.2.1 on 2020-10-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirim', '0002_auto_20201025_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='funded_price',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='funding',
            name='funding_price',
            field=models.IntegerField(max_length=100),
        ),
    ]
