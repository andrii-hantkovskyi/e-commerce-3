from django.db import models

# Create your models here.


class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('approved', 'Approved'),
        ('in_process', 'In process'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected')
    )
    DELIVERY_TYPE_CHOICES = (
        ('address', 'Address'),
        ('self_pickup', 'Self Pickup'),
        ('postal_office', 'Postal Office')
    )

    owner = models.ForeignKey(
        'users.Customer', on_delete=models.CASCADE, verbose_name='Order owner')
    cart = models.ForeignKey(
        'cart.Cart', on_delete=models.CASCADE, verbose_name='Cart')
    delivery_type = models.CharField(
        max_length=255, choices=DELIVERY_TYPE_CHOICES, verbose_name='Delivery type')
    address = models.CharField(max_length=255, verbose_name='Delivery address')
    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, verbose_name='Status', default='new')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Order created')
    last_updated = models.DateTimeField(
        auto_now=True, verbose_name='Order last updated')


    def get_formatted_str(self):
        return f'{self.owner.get_full_name()} #{self.id}'

    def __str__(self):
        return self.get_formatted_str()
