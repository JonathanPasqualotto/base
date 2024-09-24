from django.contrib import admin
from .models import Restaurant, Company, User, Category, SubCategory, Product, Order, Menu, Suggestions

admin.site.register(Restaurant)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Suggestions)

