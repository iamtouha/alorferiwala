# Generated by Django 2.2.1 on 2019-05-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20190507_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pages',
            field=models.IntegerField(default=400),
            preserve_default=False,
        ),
    ]
