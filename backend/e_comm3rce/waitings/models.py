from django.db import models


class WaitingList(models.Model):
    owner = models.OneToOneField('users.Customer', on_delete=models.CASCADE, verbose_name='List owner',
                                 related_name='waiting_list')

    class Meta:
        verbose_name = 'Waiting list'
        verbose_name_plural = 'Waiting lists'

    def get_formatted_str(self):
        return f'{self.owner.get_full_name()} #{self.id}'

    def __str__(self):
        return self.get_formatted_str()


class WaitingProduct(models.Model):
    waiting_list = models.ForeignKey(WaitingList, on_delete=models.CASCADE, verbose_name='List',
                                     related_name='products')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='Product',
                                related_name='waiting_products')

    class Meta:
        verbose_name = 'Waiting product'
        verbose_name_plural = 'Waiting products'
        unique_together = ['waiting_list', 'product']

    def __str__(self) -> str:
        return f'List #{self.waiting_list.id}, product #{self.product.id}'
