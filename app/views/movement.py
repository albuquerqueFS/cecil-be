from app.models import Movement
from app.serializers import MovementSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from drf_yasg.utils import swagger_auto_schema
from drf_spectacular.utils import extend_schema

from app.serializers.movement import CurrentBalanceSerializer
from app.utils import swagger


class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    # @swagger_auto_schema(
    #     responses={200: MovementSerializer(many=True)},
    #     manual_parameters=swagger.MOVEMENTS_GET_QUERY_PARAMS,
    # )
    @extend_schema(
        responses={200: MovementSerializer(many=True)},
    )
    def list(self, request):
        queryset = self.get_queryset().filter(user=request.user.id)
        serializer = MovementSerializer(queryset, many=True)
        return Response(serializer.data)

    # @swagger_auto_schema(
    #     responses={201: MovementSerializer()},
    #     request_body=swagger.MOVEMENTS_POST_BODY,
    # )
    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)

    # @swagger_auto_schema(
    #     responses={200: CurrentBalanceSerializer()},
    # )
    @action(detail=False, methods=["get"], url_path="balance")
    def total_positive(self, request):
        queryset = self.get_queryset().aggregate(balance=Sum("value"))
        serializer = CurrentBalanceSerializer(queryset, many=False)
        return Response(serializer.data)

    # @swagger_auto_schema(
    #     responses={200: MovementSerializer(many=True)},
    # )
    @action(detail=False, methods=["get"], url_path="income")
    def incomes(self, request):
        queryset = self.get_queryset().filter(user=request.user.id, value__gt=0)
        serializer = MovementSerializer(queryset, many=True)
        return Response(serializer.data)

    # @swagger_auto_schema(
    #     responses={200: MovementSerializer(many=True)},
    # )
    @action(detail=False, methods=["get"], url_path="expense")
    def expenses(self, request):
        queryset = self.get_queryset().filter(user=request.user.id, value__lt=0)
        serializer = MovementSerializer(queryset, many=True)
        return Response(serializer.data)
