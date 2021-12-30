# Generated by Django 3.2.9 on 2021-12-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryManager', '0002_merch'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no-img.jpeg', upload_to='product'),
        ),
        migrations.AlterField(
            model_name='merch',
            name='image',
            field=models.ImageField(default='no-img.jpeg', upload_to='merch'),
        ),
    ]
