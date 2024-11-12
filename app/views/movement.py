from app.models import Movement
from app.serializers import MovementSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from app.utils import swagger


class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    @swagger_auto_schema(
        responses={200: MovementSerializer(many=True)},
        manual_parameters=swagger.MOVEMENTS_GET_QUERY_PARAMS,
    )
    def list(self, request):
        queryset = self.get_queryset().filter(user=request.user)
        print("queryset")
        print(queryset)
        serializer = MovementSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={201: MovementSerializer()},
        request_body=swagger.MOVEMENTS_POST_BODY,
    )
    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        super().create(request, *args, **kwargs)
        return request.data
