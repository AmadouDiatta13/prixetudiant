# Generated by Django 4.1 on 2022-08-28 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='media/products/marque')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/products/product')),
                ('name', models.CharField(max_length=60)),
                ('screen', models.CharField(blank=True, max_length=60)),
                ('cpu', models.CharField(blank=True, max_length=60)),
                ('gpu', models.CharField(blank=True, max_length=60)),
                ('ram', models.CharField(blank=True, max_length=60)),
                ('space', models.CharField(blank=True, max_length=60)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('new', models.BooleanField(blank=True, default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('marque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.marque')),
            ],
        ),
    ]
