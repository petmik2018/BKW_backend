from django.urls import path, include

from rest_framework.routers import DefaultRouter

from productapp import views

router = DefaultRouter()
router.register('profile', views.ProductProfileViewSet)


urlpatterns = [
    path('', include(router.urls))
]