# Generated by Django 2.2.1 on 2019-05-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_batch_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.CharField(default='book', max_length=255),
            preserve_default=False,
        ),
    ]
