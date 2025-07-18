# Generated by Django 5.2.3 on 2025-07-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='carts.CartProduct', to='products.product'),
        ),
    ]
