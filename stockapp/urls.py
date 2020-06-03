from django.urls import path, include

from stockapp import views


urlpatterns = [
    path('<int:product_pk>/', views.StockView.as_view())
]
