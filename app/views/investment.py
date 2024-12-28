from app.models import Investment
from app.serializers import InvestmentSerializer
from rest_framework import viewsets


class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
