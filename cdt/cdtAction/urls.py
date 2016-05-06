from rest_framework.routers import DefaultRouter
from cdtAction import api

router = DefaultRouter(trailing_slash=False)

router.register(r'user', api.UserViewSet, base_name='user')

urlpatterns = router.urls

urlpatterns += []
