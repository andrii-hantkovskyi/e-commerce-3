from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from cart.serializers import RetrieveCartSerializer, CUDCartSerializer
from cart.services import get_last_cart_by_customer_id_or_create, add_product_to_cart, change_product_qty, \
    remove_product_from_cart


class CartViewSet(GenericViewSet, ListModelMixin):

    def list(self, request, *args, **kwargs):
        cart = self.get_queryset()
        serialized_data = self.get_serializer(cart).data
        return Response(status=HTTP_200_OK, data=serialized_data)

    def get_queryset(self):
        return get_last_cart_by_customer_id_or_create(self.request.user.customer.id)

    def get_serializer_class(self):
        match self.action:
            case 'create' | 'update' | 'destroy':
                return CUDCartSerializer
            case _:
                return RetrieveCartSerializer

    @action(methods=['POST'], detail=False, url_path='add-to-cart')
    def add_to_cart(self, request):
        cart_id = self.get_queryset().id
        add_product_to_cart(cart_id=cart_id, product_id=request.data.get('product_id'))
        return Response(status=HTTP_200_OK)

    @action(methods=['PATCH'], detail=False, url_path='change-qty')
    def change_qty(self, request):
        change_product_qty(cp_id=request.data.get('cp_id'), qty=request.data.get('qty'))
        serialized_data = self.get_serializer(self.get_queryset()).data
        return Response(status=HTTP_200_OK, data=serialized_data)

    @action(methods=['DELETE'], detail=False, url_path='remove-from-cart')
    def remove_from_cart(self, request):
        remove_product_from_cart(cp_id=request.data.get('cp_id'))
        return Response(status=HTTP_200_OK)
