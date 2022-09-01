from rest_framework import serializers
from .models import Candy


class CandySerializer(serializers.ModelSerializer):
    class Meta:
        model = Candy
        fields = "__all__"
