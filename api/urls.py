from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

app_name = 'api'

urlpatterns = [
    # Other URL patterns
    path('create-book/', include(router.urls)),
]