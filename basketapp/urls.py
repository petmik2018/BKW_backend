from django.urls import path, include

from basketapp import views


urlpatterns = [
    path('<int:user_pk>/', views.BasketView.as_view())
]