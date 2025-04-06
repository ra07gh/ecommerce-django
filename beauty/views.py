from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BeautyProduct

def list_beauty(request):
    beauty_items = [
        {
            'id': 1,
            'name': 'أحمر شفاه',
            'price': 120,
            'description': 'أحمر شفاه بلون جذاب يدوم طويلًا',
            'image': 'https://img.freepik.com/free-photo/red-lipstick_144627-38267.jpg'
        },
        {
            'id': 2,
            'name': 'ماسكرا ضد الماء',
            'price': 90,
            'description': 'ماسكرا مقاومة للماء لتطويل الرموش',
            'image': 'https://img.freepik.com/free-photo/black-mascara_144627-38268.jpg'
        },
        {
            'id': 3,
            'name': 'بودرة وجه حريرية',
            'price': 150,
            'description': 'بودرة خفيفة تعطي لمسة نهائية ناعمة',
            'image': 'https://img.freepik.com/free-photo/makeup-powder_144627-38270.jpg'
        },
    ]

    context = {
        'ssyd': beauty_items
    }
    template = loader.get_template('list_beauty.html')
    return HttpResponse(template.render(context, request))
from .models import BeautyProduct
from django.shortcuts import render, redirect, get_object_or_404

# إضافة للسلة
def add_to_cart(request, product_id):
    cart = request.session.get('beauty_cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['beauty_cart'] = cart
    return redirect('beauty_cart')

# عرض السلة
def view_cart(request):
    cart = request.session.get('beauty_cart', {})
    products = []
    total = 0

    for product_id, qty in cart.items():
        product = get_object_or_404(BeautyProduct, pk=product_id)
        product.qty = qty
        product.total_price = product.price * qty
        total += product.total_price
        products.append(product)

    return render(request, 'beauty/cart.html', {'products': products, 'total': total})

# حذف عنصر من السلة
def remove_from_cart(request, product_id):
    cart = request.session.get('beauty_cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['beauty_cart'] = cart
    return redirect('beauty_cart')

def products(request):
    template = loader.get_template('beauty/products.html')
    prd = BeautyProduct.objects.all()
    context = {
        'prod': prd
    }
    return HttpResponse(template.render(context, request))
def checkout(request):
    cart = request.session.get('beauty_cart', {})
    products = []
    total = 0

    for product_id, qty in cart.items():
        product = get_object_or_404(BeautyProduct, pk=product_id)
        product.qty = qty
        product.total_price = product.price * qty
        total += product.total_price
        products.append(product)

    return render(request, 'beauty/checkout.html', {'products': products, 'total': total})
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import BeautyProductForm  # حنسويه بعد شوي

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = BeautyProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('beauty_products')
    else:
        form = BeautyProductForm()
    return render(request, 'beauty/add_product.html', {'form': form})


@user_passes_test(is_admin)
def edit_product(request, product_id):
    product = BeautyProduct.objects.get(id=product_id)

    if request.method == 'POST':
        form = BeautyProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('beauty_products')
    else:
        form = BeautyProductForm(instance=product)

    return render(request, 'beauty/edit_product.html', {'form': form})

@user_passes_test(is_admin)
def delete_product(request, product_id):
    product = BeautyProduct.objects.get(id=product_id)
    product.delete()
    return redirect('beauty_products')


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # يسجل دخول مباشرة
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
        request.session['cart'] = cart
    return redirect('beauty_cart')

from .models import BeautyProduct  

def view_cart(request):
    cart = request.session.get('cart', [])
    products = BeautyProduct.objects.filter(id__in=cart)
    return render(request, 'beauty/cart.html', {'products': products})
