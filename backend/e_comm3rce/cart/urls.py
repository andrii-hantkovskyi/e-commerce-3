from rest_framework.routers import SimpleRouter

from cart.viewsets import CartViewSet

router = SimpleRouter()

router.register('', CartViewSet, basename='cart')

urlpatterns = router.urls
