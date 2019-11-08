from django.contrib import admin

from .models import *
# Register your models here.


class ModificationInline(admin.TabularInline):
    model = ProductModification
    fields = ('color', 'size')


class PhotoInline(admin.TabularInline):
    model = ProductPhoto
    fields = ('image', 'alt', 'is_main')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "category", "price", "left_in_stock", "prime_cost")
    inlines = [PhotoInline, ModificationInline]


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
