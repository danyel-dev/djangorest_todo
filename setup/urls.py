from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views
from core.views import ListViewSet, ItemViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'Lists', ListViewSet)
router.register(r'Items', ItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
