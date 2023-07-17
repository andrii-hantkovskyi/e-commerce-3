# Generated by Django 4.2.2 on 2023-07-17 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cartproduct_cart'),
        ('orders', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='cart.cart', verbose_name='Cart'),
        ),
    ]