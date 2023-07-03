from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from favorites.models import FavoriteList, FavoriteProduct


@admin.register(FavoriteList)
class FavoriteListAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_to_owner')
    list_display_links = ('id',)

    def link_to_owner(self, obj: FavoriteList):
        link = reverse("admin:users_customer_change", args=[obj.owner.id])
        return format_html('<a href="{}">{}</a>', link, obj.owner.get_full_name())
    link_to_owner.short_description = 'Owner'


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_to_list', 'link_to_product')
    list_display_links = ('id',)

    def link_to_list(self, obj: FavoriteProduct):
        link = reverse("admin:favorites_favoritelist_change",
                       args=[obj.favorite_list.id])
        return format_html('<a href="{}">{}</a>', link, obj.favorite_list.get_formatted_str())
    link_to_list.short_description = 'List'

    def link_to_product(self, obj: FavoriteProduct):
        link = reverse("admin:products_product_change", args=[obj.product.id])
        return format_html('<a href="{}">{}</a>', link, obj.product.name)
    link_to_product.short_description = 'Product'
