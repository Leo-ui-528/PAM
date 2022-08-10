from rest_framework.viewsets import ModelViewSet
from .models import Doc, Activities, Directions, City, Treaties, Customers, TypesO, State, Country
from .serializers import DocModelSerializer, ActivitiesModelSerializer, \
    DirectionsModelSerializer, CityModelSerializer, TreatiesModelSerializer, \
    CustomersModelSerializer, TypesOModelSerializer, StateOModelSerializer, \
    CountryModelSerializer


class DocModelViewSet(ModelViewSet):
    queryset = Doc.objects.all()
    serializer_class = DocModelSerializer


class ActivitiesModelViewSet(ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesModelSerializer


class DirectionsModelViewSet(ModelViewSet):
    queryset = Directions.objects.all()
    serializer_class = DirectionsModelSerializer


class CityModelViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer
    filterset_fields = ['name']


class TreatiesModelViewSet(ModelViewSet):
    queryset = Treaties.objects.all()
    serializer_class = TreatiesModelSerializer


class CustomersModelViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersModelSerializer
    filterset_fields = ['name']


class TypesOModelViewSet(ModelViewSet):
    queryset = TypesO.objects.all()
    serializer_class = TypesOModelSerializer


class StateModelViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateOModelSerializer


class CountryModelViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer

