from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from specifications.models import Specification


class SpecificationSerializer(ModelSerializer):
    name = SerializerMethodField()
    measurement_unit = SerializerMethodField()

    class Meta:
        model = Specification
        fields = ('name', 'measurement_unit', 'value')

    def get_name(self, obj):
        return obj.category.name

    def get_measurement_unit(self, obj):
        return obj.category.measurement_unit
