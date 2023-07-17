from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from products.models import Product
from specifications.serializers import SpecificationSerializer


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()
    specifications = SpecificationSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'category', 'specifications', 'name', 'price', 'image', 'is_available')

    def get_category(self, obj):
        return obj.category.name
