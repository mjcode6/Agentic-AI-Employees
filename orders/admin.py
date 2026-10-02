from django.contrib import admin
from .models import Product, Order, RefundRequest


class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'in_stock']
    
class orderAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'product_name', 'amount', 'status', 'carrier', 'tracking_number',]
    
class refundRequestAdmin(admin.ModelAdmin):
    list_display = ['order', 'user', 'reason', 'status','created_at']
    
    



admin.site.register(Product, productAdmin)
admin.site.register(Order, orderAdmin)
admin.site.register(RefundRequest, refundRequestAdmin)
