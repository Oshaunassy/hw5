# Generated by Django 4.2.11 on 2024-04-03 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_produced_alter_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='produced',
            field=models.DateField(default=datetime.datetime(2024, 4, 3, 19, 50, 16, 435477)),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(verbose_name=(1, 2, 3, 4, 5)),
        ),
    ]
