# Generated by Django 3.2.6 on 2021-09-22 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productimage_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product'),
        ),
    ]
