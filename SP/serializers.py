from rest_framework import serializers

from SP.models import SP


class SPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SP
        fields = "__all__"
