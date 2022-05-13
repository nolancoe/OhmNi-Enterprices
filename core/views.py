from django.shortcuts import render
from django.conf import settings
from store.utils import cookieCart, cartData, guestOrder

DEBUG = False

def home_screen_view(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = "1"
    return render(request, "core/home.html", context)
