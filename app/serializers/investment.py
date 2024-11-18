from rest_framework import serializers

from app.models import Investment


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = "__all__"


class InvestmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ["value", "name", "types", "category"]
