from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from orders.serializers import OrderSerializer
from orders.services import get_customer_orders, get_customer_order, create_new_order


class OrdersViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        serialized_data = self.get_serializer(data, many=True).data
        return Response(status=HTTP_200_OK, data=serialized_data)

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        data = get_customer_order(order_id=pk, customer_id=request.user.customer.id)
        serialized_data = self.get_serializer(data).data
        return Response(status=HTTP_200_OK, data=serialized_data)

    def get_queryset(self):
        return get_customer_orders(self.request.user.customer.id)

    @action(methods=['POST'], detail=False, url_path='create-order')
    def create_order(self, request):
        try:
            customer_id, cart_id, delivery_type, address = request.user.customer.id, request.data.get(
                'cart_id'), request.data.get('delivery_type'), request.data.get('address')
            create_new_order(customer_id=customer_id, cart_id=cart_id, delivery_type=delivery_type, address=address)
            return Response(status=HTTP_201_CREATED)
        except ValueError as e:
            return Response(status=HTTP_400_BAD_REQUEST, data={'error': str(e)})
