from django.db import models


class SpecificationCategory(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Specification category slug')
    name = models.CharField(max_length=255, verbose_name='Specification category name')
    measurement_unit = models.CharField(max_length=255, verbose_name='Unit of measurement')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Specification category'
        verbose_name_plural = 'Specification categories'

class Specification(models.Model):
    category = models.ForeignKey(SpecificationCategory, on_delete=models.CASCADE, verbose_name='Specification category', related_name='specifications')
    value = models.CharField(max_length=255, verbose_name='Value')

    def __str__(self):
        return f'{self.category.name} {self.value}'
    
class ProductCategory(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Product category slug')
    name = models.CharField(max_length=255, verbose_name='Product category name')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'
    

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Product category', related_name='products')
    specifications = models.ManyToManyField(Specification, verbose_name='Product specifications', related_name='products')
    name = models.CharField(max_length=255, verbose_name='Product name')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Product price')
    description = models.TextField(verbose_name='Product description')
    image = models.ImageField(verbose_name='Product image', null=True, blank=True)
    is_available = models.BooleanField(default=True, verbose_name='Is product available')

    def __str__(self):
        return self.name
    

