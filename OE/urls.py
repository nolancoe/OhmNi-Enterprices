"""BodiedByLove URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from core.views import (
    home_screen_view
)

from account.views import (
    register_view,
    login_view,
    logout_view,

)

from services.views import (
    death_coach_view,
    life_coach_view,
    qi_gong_view,
    rune_reading_view,
    hypnotherapy_view,
    grief_work_view,
    end_of_life_care_view,
)

from store.views import (

    store_view,
    cart_view,
    checkout_view,
    ProductDetailView,
    updateItem,
    processOrder,
    orders_view,
    OrderDetailView,

)

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('', include('services.urls')),
    path('account/', include('account.urls', namespace='account')),
    path('store', include('store.urls', namespace='store')),
    path('23456745674464667/', admin.site.urls),
    path('career_life_coach', death_coach_view, name='career_life_coach'),
    path('end_of_life_care', end_of_life_care_view, name='end_of_life_care'),
    path('grief_work', grief_work_view, name='grief_work'),
    path('life_coach', life_coach_view, name='life_coach'),
    path('hypnotherapy', hypnotherapy_view, name='hypnotherapy'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('qi_gong', qi_gong_view, name='qi_gong'),
    path('register/', register_view, name="register"),
    path('rune_reading', rune_reading_view, name='rune_reading'),

    #path('update_item/', updateItem, name="update_item"),
    #path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    #path('process_order/', processOrder, name="process_order"),
    #path('store/', store_view, name="store"),
    #path('cart/', cart_view, name="cart"),
    #path('checkout/', checkout_view, name="checkout"),

    #path('order/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    #path('orders', orders_view.as_view(), name='orders'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Configure admin titles

admin.site.site_header = "OhmNi Enterprices Admin Page"
admin.site.site_title = "OhmNi Enterprices"
admin.site.index_title = "Administration"
