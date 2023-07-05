from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_to_owner', 'link_to_cart',
                    'delivery_type', 'status', 'created', 'last_updated')
    list_display_links = ('id',)
    list_editable = ('status',)
    list_filter = ('delivery_type', 'status', 'created', 'last_updated')
    ordering = ('created', 'last_updated')
    readonly_fields = ('created', 'last_updated')

    def link_to_owner(self, obj: Order):
        link = reverse("admin:users_customer_change", args=[obj.owner.id])
        return format_html('<a href="{}">{}</a>', link, obj.owner.get_full_name())
    link_to_owner.short_description = 'Owner'

    def link_to_cart(self, obj: Order):
        link = reverse("admin:cart_cart_change", args=[obj.cart.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.cart.get_formatted_str()}')
    link_to_cart.short_description = 'Cart'
