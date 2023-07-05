from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from users.models import Customer
from users.permissions import IsAuthenticatedOrCreateOnly
from users.serializers import CustomerSerializer
from users.services import register_new_customer, update_customer_info


class CustomerViewSet(CreateModelMixin,
                      GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticatedOrCreateOnly]

    def create(self, request, *args, **kwargs):
        try:
            email, password, first_name, last_name, phone = request.data.get('email'), request.data.get(
                'password'), request.data.get('first_name'), request.data.get('last_name'), request.data.get('phone')

            register_new_customer(email, password, first_name, last_name, phone)

            return Response(status=HTTP_201_CREATED)
        except Exception as ex:
            return Response(status=HTTP_400_BAD_REQUEST, data=ex)

    @action(detail=False, methods=['GET'], url_path='get-profile')
    def get_profile(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(request.user.customer).data
        return Response(status=HTTP_200_OK, data=serialized_data)

    @action(detail=False, methods=['PUT', 'PATCH'], url_path='update-profile')
    def update_profile(self, request, *args, **kwargs):
        try:
            email, first_name, last_name, phone = request.data.get('email'), request.data.get(
                'first_name'), request.data.get('last_name'), request.data.get('phone')

            customer = update_customer_info(request.user.customer, email, first_name, last_name, phone)
            serialized_data = self.get_serializer(customer).data

            return Response(status=HTTP_200_OK, data=serialized_data)
        except Exception as ex:
            return Response(status=HTTP_400_BAD_REQUEST, data=ex)
