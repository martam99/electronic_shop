from rest_framework import serializers

from employee.permissions import UserPermissionsAll
from factory.models import Factory


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ['title', 'head', 'address', 'phone', 'fax', 'mail', 'production']
        permission_classes = [UserPermissionsAll]


