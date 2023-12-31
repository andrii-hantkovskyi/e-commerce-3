# Generated by Django 4.2.2 on 2023-07-03 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_is_admin_user_is_staff'),
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritelist',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customer', verbose_name='List owner'),
        ),
    ]
