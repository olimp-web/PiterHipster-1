from django.contrib import admin

from .models import Order, OrderStatusChangeLog

# Register your models here.


class OrderHistoryInline(admin.TabularInline):
    readonly_fields = ('status', 'timestamp')
    model = OrderStatusChangeLog
    extra = 0
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'total_cost')
    inlines = (OrderHistoryInline, )