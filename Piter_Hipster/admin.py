from django.contrib import admin
from Piter_Hipster.models import *

class GoodsAdmin(admin.ModelAdmin):
    list_display = ("id", "Title", "Description", "id_category", "Price", "Left_in_stock", "Prime_cost")
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "Title")
class PhotosAdmin(admin.ModelAdmin):
    list_display=("id", "Direction", "isMain")
class ModificationsAdmin(admin.ModelAdmin):
    list_display = ("id", "color", "size")

class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "Lastname", "Middlename", "Phone", "email", "id_delivery", "Address", "status", "Index",
                  "Date_of_order", "Comment")
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("id", "Type_delivery", "Address", "Price")

class GoodsInOrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "id_goods", "id_order", "Price")


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Photos, PhotosAdmin)
admin.site.register(Modifications, ModificationsAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(GoodsInOrders, GoodsInOrdersAdmin)
