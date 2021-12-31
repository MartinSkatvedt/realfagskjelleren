# Generated by Django 3.2.9 on 2021-12-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('amount', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='merch')),
            ],
        ),
    ]