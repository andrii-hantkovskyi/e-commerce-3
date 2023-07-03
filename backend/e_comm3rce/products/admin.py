from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from products.models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link_to_category', 'price', 'is_available')
    list_display_links = ('id', 'name')
    list_filter = ('price', 'is_available')
    list_editable = ('price', 'is_available')

    def link_to_category(self, obj: Product):
        link = reverse("admin:products_productcategory_change",
                       args=[obj.category.id])
        return format_html('<a href="{}">{}</a>', link, obj.category.name)
    link_to_category.short_description = 'Category'
