from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'', CartItemViewSet)

app_name = 'api'

urlpatterns = [
    # Other URL patterns
    path('add/', include(router.urls)),
    path('cart/', include(router.urls)),
    
]