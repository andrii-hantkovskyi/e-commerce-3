from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from specifications.models import SpecificationCategory, Specification


@admin.register(SpecificationCategory)
class SpecificationCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_display_links = ('id', 'name')


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_to_speccat', 'f_value')
    list_display_links = ('id',)

    def link_to_speccat(self, obj: Specification):
        link = reverse("admin:specifications_specificationcategory_change", args=[
                       obj.category.id])
        return format_html('<a href="{}">{}</a>', link, obj.category.name)
    link_to_speccat.short_description = 'Spec name'

    @admin.display(description='Formatted value')
    def f_value(self, obj: Specification):
        return f'{obj.value}{obj.category.measurement_unit}'
