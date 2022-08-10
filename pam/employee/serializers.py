from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Employee, Owner


class EmployeeModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class OwnerModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
