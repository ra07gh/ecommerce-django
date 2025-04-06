from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# استيراد العروض من التطبيقات
from home import views as _home
from electronic import views as _electronic
from beauty.views import (
    list_beauty, products as beauty_products, add_to_cart,
    view_cart, remove_from_cart, edit_product, delete_product,
    add_product, register
)
from home.views import checkout
from home.views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحات الرئيسية
    path('', _home.showland),
    path('checkout/', checkout, name='checkout'),

    # أقسام المنتجات
    path('beauty/', list_beauty, name='list_beauty'),
    path('beauty/products/', beauty_products, name='beauty_products'),
    path('beauty/add_to_cart/<int:product_id>/', add_to_cart, name='beauty_add_to_cart'),
    path('beauty/cart/', view_cart, name='beauty_cart'),
    path('beauty/remove_from_cart/<int:product_id>/', remove_from_cart, name='beauty_remove_from_cart'),
    path('beauty/edit/<int:product_id>/', edit_product, name='beauty_edit'),
    path('beauty/delete/<int:product_id>/', delete_product, name='beauty_delete'),
    path('beauty/add/', add_product, name='beauty_add'),

    path('electronic/', _electronic.list_elctronic, name='list_electronics'),
    path('showphone/<str:phone>/', _electronic.showphone, name='showphone'),
    path('categories/', _electronic.categories, name='categories'),
    path('products/', _electronic.products),

    # تسجيل الدخول والخروج والتسجيل
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', register, name='register'),

    # صفحات إضافية
    path('accounts/', include('home.urls')),
]

# الصور وملفات media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
