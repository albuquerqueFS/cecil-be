from rest_framework import routers
from app.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)