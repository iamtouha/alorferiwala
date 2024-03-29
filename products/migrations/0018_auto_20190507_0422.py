# Generated by Django 2.2.1 on 2019-05-06 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_product_ordered_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='upload_date',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='product',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
