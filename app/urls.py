from rest_framework import routers
from app.views import UserViewSet, MovementViewSet, InvestmentViewSet, RegisterView

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"movements", MovementViewSet)
router.register(r"investments", InvestmentViewSet)
