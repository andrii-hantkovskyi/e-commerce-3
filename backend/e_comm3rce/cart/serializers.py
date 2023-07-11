from rest_framework.serializers import ModelSerializer

from cart.models import Cart, CartProduct


class CartProductSerializer(ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('id', 'product_id', 'qty', 'total_price')


class CartSerializer(ModelSerializer):
    products = CartProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('products', 'total_price')
