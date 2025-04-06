from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from beauty.models import BeautyProduct
from .models import Order, OrderItem


def showland(request):
    return render(request, 'home/landpage.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('/')


def view_cart(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = BeautyProduct.objects.filter(id__in=product_ids)

    cart_items = []
    for product in products:
        quantity = cart[str(product.id)]
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity,
        })

    total_price = sum(item['total'] for item in cart_items)

    return render(request, 'home/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {}
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    request.session['cart'] = cart
    return redirect('cart')


def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
        request.session['cart'] = cart
    return redirect('cart')


def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        if cart[product_id_str] > 1:
            cart[product_id_str] -= 1
        else:
            del cart[product_id_str]
        request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')


def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = BeautyProduct.objects.get(id=product_id)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total
        })

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        request.session['payment_method'] = payment_method
        return redirect('confirm_order')

    return render(request, 'home/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


@login_required
def confirm_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')

    payment_method = request.session.get('payment_method', 'cash')
    
    total_price = 0
    order = Order.objects.create(
        user=request.user,
        total_price=0,
        payment_method=payment_method  # هذا يعتمد على وجوده في models.py
    )

    for product_id, quantity in cart.items():
        product = BeautyProduct.objects.get(id=product_id)
        item_total = product.price * quantity
        total_price += item_total

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )

    order.total_price = total_price
    order.save()
    request.session['cart'] = {}

    return redirect('invoice', order_id=order.id)


@login_required
def invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = order.items.all() 

    return render(request, 'home/invoice.html', {
        'order': order,
        'items': items 
    })
