# Generated by Django 2.2.1 on 2019-05-05 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_current_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publish_year',
            field=models.IntegerField(default=1998, validators=[django.core.validators.MaxLengthValidator(4), django.core.validators.MinLengthValidator(4)]),
            preserve_default=False,
        ),
    ]
