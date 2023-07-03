from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from cart.models import Cart, CartProduct

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_to_owner', 'total_price', 'last_updated')
    list_display_links = ('id',)
    list_filter = ('total_price', 'last_updated')
    ordering = ('-last_updated',)
    readonly_fields = ('total_price',)

    def link_to_owner(self, obj: Cart):
        link = reverse("admin:users_customer_change", args=[obj.owner.id])
        return format_html('<a href="{}">{}</a>', link, obj.owner.get_full_name())
    link_to_owner.short_description = 'Owner'

@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_to_cart', 'link_to_product', 'qty', 'total_price')
    list_display_links = ('id',)
    readonly_fields = ('total_price',)

    def link_to_cart(self, obj: CartProduct):
        link = reverse("admin:cart_cart_change", args=[obj.cart.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.cart.get_formatted_str()}')
    link_to_cart.short_description = 'Cart'

    def link_to_product(self, obj: CartProduct):
        link = reverse("admin:products_product_change", args=[obj.product.id])
        return format_html('<a href="{}">{}</a>', link, obj.product.name)
    link_to_product.short_description = 'Product'