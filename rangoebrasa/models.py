from email.policy import default

from django.db import models
import uuid
from datetime import datetime

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateField(default=datetime.now)
    active = models.BooleanField(default=True)

    # Relacionamentos
    order = models.ManyToManyField('Order', blank=True, related_name='restaurants_orders')
    menu = models.ManyToManyField('Menu', blank=True, related_name='restaurants_menu')
    users = models.ManyToManyField('User', blank=True, related_name='restaurants_users')
    categories = models.ManyToManyField('Category', blank=True, related_name='restaurants_categories')
    companies = models.ManyToManyField('Company', blank=True, related_name='restaurants_companies')
    products = models.ManyToManyField('Product', blank=True, related_name='restaurants_products')
    suggestions = models.ManyToManyField('Suggestions', blank=True, related_name='restaurants_suggestions')


    class Meta:
        db_table = "restaurant"


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='company_items')

    # Relacionamento com User
    users = models.ManyToManyField('User', blank=True, related_name='companies_users')

    class Meta:
        db_table = "company"


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255, unique=True)
    date_birth = models.DateField(null=True, blank=True)
    cellphone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.now)

    # Relacionamentos
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_restaurants')
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_companies')
    orders = models.ManyToManyField('Order', blank=True, related_name='users_orders')

    class Meta:
        db_table = "users"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='category_items')

    # Relacionamento com SubCategory e Product
    subcategories = models.ManyToManyField('SubCategory', blank=True, related_name='category_subcategories')
    products = models.ManyToManyField('Product', blank=True, related_name='category_products')

    class Meta:
        db_table = "category"


class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory_category_items')

    class Meta:
        db_table = "subcategory"


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    exhibit = models.BooleanField(default=True)

    # Relacionamentos
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='product_categories')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='product_restaurants')
    orders = models.ManyToManyField('Order', blank=True, related_name='product_orders')

    class Meta:
        db_table = "product"


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(default=datetime.now)
    status = models.IntegerField(default=0, null=True, blank=True)
    amount = models.IntegerField()
    amount_product = models.IntegerField(null=True, blank=True)

    # Relacionamentos
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='order_product_items')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user_items')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='order_restaurant_items')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='order_menu_items')

    class Meta:
        db_table = "orders"


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    created_at = models.DateField(default=datetime.now)

    # Relacionamento com Restaurant
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_restaurant_items')

    class Meta:
        db_table = "menu"


class Suggestions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    exhibit = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.now)

    # Relacionamento com Restaurant
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='suggestions_restaurant_items')

    class Meta:
        db_table = "suggestions"
