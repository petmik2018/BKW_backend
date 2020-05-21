from django.urls import path, include

from rest_framework.routers import DefaultRouter

from seller_api import views

router = DefaultRouter()
router.register('profile', views.SellerProfileViewSet)


urlpatterns = [
    path('', include(router.urls))
]