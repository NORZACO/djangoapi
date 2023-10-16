# Generated by Django 4.2.6 on 2023-10-16 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('sale_start', models.DateTimeField(blank=True, default=None, null=True)),
                ('sale_end', models.DateTimeField(blank=True, default=None, null=True)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='products')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('picture', models.ImageField(default='https://i.pinimg.com/originals/0d/cf/e6/0dcfe624b9b7285ac51d8ba5fd002d71.jpg', upload_to='quiz_pictures/')),
                ('answer', models.CharField(max_length=255)),
                ('description', models.TextField(default='No description')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart_items', related_query_name='shopping_cart_item', to='store.shoppingcart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='store.product')),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', related_query_name='item', to='store.shoppingcart')),
            ],
        ),
    ]
