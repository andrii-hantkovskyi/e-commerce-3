from rest_framework.serializers import ModelSerializer

from cart.models import Cart, CartProduct
from products.serializers import ProductSerializer


class RetrieveCartProductSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartProduct
        fields = ('id', 'product', 'qty', 'total_price')


class CreateCartProductSerializer(ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('id', 'product_id', 'qty')


class RetrieveCartSerializer(ModelSerializer):
    products = RetrieveCartProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('products', 'total_price')


class CUDCartSerializer(ModelSerializer):
    products = CreateCartProductSerializer(many=True)
    fields = ('products',)
