from django.shortcuts import render, redirect,HttpResponseRedirect, reverse
import time
# Create your views here.
from carts.models import CartItem, Cart
from .models import Order
import string
import random
# from django.contrib.auth import get_user_model

# user = get_user_model()

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))
    try:
        order = Order.objects.get(order_id = the_id)
        id_generator()
    except Order.DoesNotExist:
        return the_id

def orders(request):
    return render(request, 'orders/user.html', context=None)

def checkout(request):
    try:
        the_id = request.session['cart_id']
        print(the_id)
        cart = CartItem.objects.get(id=the_id)
        cartTotal = Cart.objects.get(id=the_id)
        print(cart)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('carts:cart'))

    try:
        new_order = Order.objects.get(cart = cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.final_total = cartTotal.total
        new_order.location = request.user.profile.location
        new_order.order_id = id_generator()
        new_order.save()


    if new_order.status == "Finished":
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse('carts:cart'))


    return render(request, 'mainapp/index.html', context=None)
