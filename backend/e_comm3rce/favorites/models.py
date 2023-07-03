from django.db import models


class FavoriteList(models.Model):
    owner = models.OneToOneField('users.Customer', on_delete=models.CASCADE, verbose_name='List owner', related_name='favorite_list')


    class Meta:
        verbose_name = 'Favorite list'
        verbose_name_plural = 'Favorite lists'

    def get_formatted_str(self):
        return f'{self.owner.get_full_name()} #{self.id}'

    def __str__(self):
        return self.get_formatted_str()
    

class FavoriteProduct(models.Model):
    favorite_list = models.ForeignKey(FavoriteList, on_delete=models.CASCADE, verbose_name='List', related_name='products')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='Product', related_name='favorite_products')


    class Meta:
        verbose_name = 'Favorite product'
        verbose_name_plural = 'Favorite products'

    def __str__(self) -> str:
        return f'List #{self.favorite_list.id}, product #{self.product.id}'
