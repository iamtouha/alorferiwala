# Generated by Django 2.2.1 on 2019-05-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20190505_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(max_length=255, upload_to='photos/%Y/%m/%d'),
        ),
    ]
