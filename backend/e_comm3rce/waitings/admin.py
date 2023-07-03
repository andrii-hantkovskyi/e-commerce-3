from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from waitings.models import WaitingList, WaitingProduct


@admin.register(WaitingList)
class WaitingListAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_to_owner')
    list_display_links = ('id',)

    def link_to_owner(self, obj: WaitingList):
        link = reverse("admin:users_customer_change", args=[obj.owner.id])
        return format_html('<a href="{}">{}</a>', link, obj.owner.get_full_name())
    link_to_owner.short_description = 'Owner'


@admin.register(WaitingProduct)
class WaitingProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_to_list', 'link_to_product')
    list_display_links = ('id',)

    def link_to_list(self, obj: WaitingProduct):
        link = reverse("admin:waitings_waitinglist_change",
                       args=[obj.waiting_list.id])
        return format_html('<a href="{}">{}</a>', link, obj.waiting_list.get_formatted_str())
    link_to_list.short_description = 'List'

    def link_to_product(self, obj: WaitingProduct):
        link = reverse("admin:products_product_change", args=[obj.product.id])
        return format_html('<a href="{}">{}</a>', link, obj.product.name)
    link_to_product.short_description = 'Product'
