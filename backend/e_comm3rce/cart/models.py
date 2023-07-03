from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.

class Cart(models.Model):
    owner = models.ForeignKey("users.Customer", on_delete=models.CASCADE, related_name='carts', verbose_name="Cart owner")
    total_price = models.DecimalField(verbose_name="Total price", decimal_places=2, max_digits=10, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def get_formatted_str(self):
        f'{self.owner.get_full_name()} #{self.id}'

    def __str__(self) -> str:
        return self.get_formatted_str()
    
    def save(self, *args, **kwargs):
        if self.id:
            self.total_price = sum([cart_product.total_price for cart_product in self.products.all()])
        return super().save(*args, **kwargs)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products', verbose_name="Cart")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="cart_products", verbose_name="Product")
    qty = models.PositiveIntegerField(verbose_name="Product quantity")
    total_price = models.DecimalField(verbose_name="Total price", decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Cart product'
        verbose_name_plural = 'Cart products'

    def __str__(self) -> str:
        return f'Cart #{self.cart.id}, product ${self.product.id}'
    
    def save(self, *args, **kwargs):
        self.total_price = self.qty * self.product.price
        return super().save(*args, **kwargs)

@receiver(post_save, sender=CartProduct, dispatch_uid="recalculated_total_price")
def recalculate_total_price(sender, instance, **kwargs):
    instance.cart.save()