from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Doc, Activities, Directions, City, Treaties, Customers, TypesO, State, Country


class CityModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class DocModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'


class ActivitiesModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'


class DirectionsModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Directions
        fields = '__all__'


class TreatiesModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Treaties
        fields = '__all__'


class CustomersModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class TypesOModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TypesO
        fields = '__all__'


class StateOModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CountryModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


