from rest_framework import serializers

from employee.permissions import UserPermissionsAll
from supplier.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        permission_classes = [UserPermissionsAll]

