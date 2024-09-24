# Generated by Django 5.1.1 on 2024-09-23 02:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('amount', models.IntegerField()),
                ('amount_product', models.IntegerField(blank=True, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_menu_items', to='rangoebrasa.menu')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('exhibit', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_categories', to='rangoebrasa.category')),
                ('orders', models.ManyToManyField(blank=True, related_name='product_orders', to='rangoebrasa.order')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_product_items', to='rangoebrasa.product'),
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='category_products', to='rangoebrasa.product'),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=255, unique=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='restaurants_categories', to='rangoebrasa.category')),
                ('companies', models.ManyToManyField(blank=True, related_name='restaurants_companies', to='rangoebrasa.company')),
                ('menu', models.ManyToManyField(blank=True, related_name='restaurants_menu', to='rangoebrasa.menu')),
                ('order', models.ManyToManyField(blank=True, related_name='restaurants_orders', to='rangoebrasa.order')),
                ('products', models.ManyToManyField(blank=True, related_name='restaurants_products', to='rangoebrasa.product')),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_restaurants', to='rangoebrasa.restaurant'),
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_restaurant_items', to='rangoebrasa.restaurant'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_restaurant_items', to='rangoebrasa.restaurant'),
        ),
        migrations.AddField(
            model_name='company',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_items', to='rangoebrasa.restaurant'),
        ),
        migrations.AddField(
            model_name='category',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_items', to='rangoebrasa.restaurant'),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory_category_items', to='rangoebrasa.category')),
            ],
            options={
                'db_table': 'subcategory',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='subcategories',
            field=models.ManyToManyField(blank=True, related_name='category_subcategories', to='rangoebrasa.subcategory'),
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('exhibit', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestions_restaurant_items', to='rangoebrasa.restaurant')),
            ],
            options={
                'db_table': 'suggestions',
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='suggestions',
            field=models.ManyToManyField(blank=True, related_name='restaurants_suggestions', to='rangoebrasa.suggestions'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=255, unique=True)),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('cellphone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_companies', to='rangoebrasa.company')),
                ('orders', models.ManyToManyField(blank=True, related_name='users_orders', to='rangoebrasa.order')),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_restaurants', to='rangoebrasa.restaurant')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='restaurants_users', to='rangoebrasa.user'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user_items', to='rangoebrasa.user'),
        ),
        migrations.AddField(
            model_name='company',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='companies_users', to='rangoebrasa.user'),
        ),
    ]
