from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import Customer


class CustomerSerializer(ModelSerializer):
    email = SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('email', 'first_name', 'last_name', 'phone_number')

    def get_email(self, obj):
        return obj.user.email
