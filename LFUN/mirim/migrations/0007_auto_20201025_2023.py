# Generated by Django 2.2.1 on 2020-10-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirim', '0006_auto_20201025_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='funded_price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='funding',
            name='funding_price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
