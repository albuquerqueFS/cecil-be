from app.models import Movement
from app.serializers import MovementSerializer
from rest_framework import viewsets

class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer