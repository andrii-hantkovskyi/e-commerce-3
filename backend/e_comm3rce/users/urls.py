from rest_framework.routers import SimpleRouter

from users.viewsets import CustomerViewSet

router = SimpleRouter()

router.register('customers', CustomerViewSet, 'customers')

urlpatterns = router.urls
