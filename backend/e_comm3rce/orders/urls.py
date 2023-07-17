from rest_framework.routers import SimpleRouter

from orders.viewsets import OrdersViewSet

router = SimpleRouter()

router.register('', OrdersViewSet, basename='orders')

urlpatterns = router.urls
