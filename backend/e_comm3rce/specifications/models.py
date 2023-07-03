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