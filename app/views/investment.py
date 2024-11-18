from app.models import Investment
from app.serializers import InvestmentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from app.serializers.investment import InvestmentPostSerializer
from app.utils import swagger


class InvestmentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    # @swagger_auto_schema(
    #     responses={201: InvestmentSerializer()},
    #     request_body=swagger.INVESTMENT_POST_BODY,
    # )
    # def create(self, request):
    #     request.data["user"] = request.user.id
    #     serializer = InvestmentPostSerializer(data=request.data)

    #     serializer.is_valid(raise_exception=True)

    #     investment = Investment.objects.create(**serializer.data)
    #     return Response(investment)
