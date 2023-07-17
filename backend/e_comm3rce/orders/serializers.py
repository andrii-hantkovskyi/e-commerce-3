from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from cart.serializers import RetrieveCartProductSerializer
from orders.models import Order


class OrderSerializer(ModelSerializer):
    products = SerializerMethodField()
    total_price = SerializerMethodField()
    delivery_type = SerializerMethodField()
    status = SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'products', 'total_price', 'delivery_type', 'address', 'status')

    def get_products(self, obj):
        products = obj.cart.products.all()
        serialized_data = RetrieveCartProductSerializer(products, many=True).data
        return serialized_data

    def get_total_price(self, obj):
        return obj.cart.total_price

    def get_delivery_type(self, obj):
        return dict(obj.DELIVERY_TYPE_CHOICES).get(obj.delivery_type)

    def get_status(self, obj):
        return dict(obj.STATUS_CHOICES).get(obj.status)

