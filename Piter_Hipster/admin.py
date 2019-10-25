from django.contrib import admin
from Piter_Hipster.models import *

class GoodsAdmin(admin.ModelAdmin):
    list_display = ("id", "Title", "Description", "id_category", "Price", "Left_in_stock", "Prime_cost")
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "Title")
class PhotosAdmin(admin.ModelAdmin):
    list_display=("id", "Direction")


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Photos, PhotosAdmin)