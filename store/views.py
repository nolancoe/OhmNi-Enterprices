from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from django.views.generic import ListView, DetailView, CreateView

def store_view(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)


def cart_view(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout_view(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)


    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = request.user, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()



    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)




def processOrder(request):
    transaction_id = datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:

        order, created = Order.objects.get_or_create(customer = request.user, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
        customer=request.user,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_details.html'


class orders_view(ListView):
    context_object_name = 'order_list'
    template_name = 'store/orders.html'
    queryset = Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super(orders_view, self).get_context_data(**kwargs)
        context['shippingaddress'] = ShippingAddress.objects.all()
        context['orderitem'] = OrderItem.objects.all()
        context['order'] = Order.objects.all()

        return context

class OrderDetailView(DetailView):
    model = Order
    template_name = 'store/order_details.html'


