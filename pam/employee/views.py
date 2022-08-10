from rest_framework.viewsets import ModelViewSet
from .models import Employee, Owner
from .serializers import EmployeeModelSerializer, OwnerModelSerializer


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    filterset_fields = ['employee']


class OwnerModelViewSet(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerModelSerializer
