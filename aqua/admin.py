from django.contrib import admin
from aqua.models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = []
    search_fields = ['name', 'price']
    fieldsets = (
        ('Product Details', {'fields': ('name', 'description', 'describe_1', 'describe_2', 'describe_3', 'price', 'image')}),
    )
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile')
    list_filter = ['request_from']
    search_fields = ['name', 'email', 'mobile']
    fieldsets = (
        ('Contact Details', {'fields': ('name', 'email', 'mobile', 'company_name', 'subject', 'message', 'request_from', 'date_time')}),
    )
    readonly_fields = ['date_time']

@admin.register(Qutation_for_product)
class Qutation_for_productAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'email', 'mobile')
    list_filter = []
    search_fields = ['product__name', 'name', 'email', 'mobile']
    fieldsets = (
        ('Contact Details', {'fields': ('product', 'name', 'email', 'mobile', 'subject', 'message', 'date_time')}),
    )
    readonly_fields = ['date_time']