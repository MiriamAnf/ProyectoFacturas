# Generated by Django 3.1.2 on 2020-12-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linereceipt',
            name='units',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='linereceipt',
            name='unit_price',
            field=models.IntegerField(),
        ),
    ]