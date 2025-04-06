from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import add_to_cart, view_cart
from .views import add_to_cart, view_cart, increase_quantity
from .views import remove_from_cart
from .views import decrease_quantity
from .views import checkout
from .views import confirm_order
from .views import invoice
from .views import custom_logout

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', custom_logout, name='logout'),
    path('cart/', view_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('increase_quantity/<int:product_id>/', increase_quantity, name='increase_quantity'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('decrease_quantity/<int:product_id>/', decrease_quantity, name='decrease_quantity'),
    path('checkout/', checkout, name='checkout'),
    path('confirm_order/', confirm_order, name='confirm_order'),
    path('invoice/<int:order_id>/', invoice, name='invoice'),

]
