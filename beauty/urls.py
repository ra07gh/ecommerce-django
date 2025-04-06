from django.urls import path
from . import views
from .views import view_cart

urlpatterns = [
    path('', views.list_beauty, name='list_beauty'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
