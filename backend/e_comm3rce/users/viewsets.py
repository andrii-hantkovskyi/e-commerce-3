from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import GenericViewSet

from users.models import Customer
from users.permissions import IsAuthenticatedOrCreateOnly
from users.serializers import CustomerSerializer
from users.services import register_new_customer


class CustomerViewSet(CreateModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticatedOrCreateOnly]

    def create(self, request, *args, **kwargs):
        email, password, first_name, last_name, phone = request.data.get('email'), request.data.get(
            'password'), request.data.get('first_name'), request.data.get('last_name'), request.data.get('phone')

        try:
            register_new_customer(email, password, first_name, last_name, phone)
            return Response(status=HTTP_201_CREATED)
        except Exception as ex:
            return Response(status=HTTP_400_BAD_REQUEST, data=ex)
