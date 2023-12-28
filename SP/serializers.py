from rest_framework import serializers

from SP.models import SP
from employee.permissions import UserPermissionsAll


class SPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SP
        fields = "__all__"

