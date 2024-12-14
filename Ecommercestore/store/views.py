from django.shortcuts import render

from django.http import HttpResponse

## test function
def test(request):
    return HttpResponse(" store app is connected")


from django.shortcuts import render, redirect
from .models import Category, Product, Cart, Wishlist
from django.contrib.auth.decorators import login_required

def main_page(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "store/main_page.html", context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "store/product_detail.html", context)

@login_required
def dashboard(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "store/dashboard.html", context)

@login_required
def cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    context = {"cart_products": cart.product.all()}
    return render(request, "store/cart.html", context)

@login_required
def wishlist(request):
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    context = {"wishlist_products": wishlist.product.all()}
    return render(request, "store/wishlist.html", context)

@login_required
def add_to_wishlist(request, pk):
    product = Product.objects.get(pk=pk)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist.product.add(product)
    return redirect("wishlist")

@login_required
def remove_from_wishlist(request, pk):
    product = Product.objects.get(pk=pk)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.product.remove(product)
    return redirect("wishlist")



@login_required
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    user_cart, _ = Cart.objects.get_or_create(user=request.user)  # Renamed the variable to user_cart
    user_cart.product.add(product)
    return redirect("cart")

@login_required
def remove_from_cart(request, pk):
    product = Product.objects.get(pk=pk)
    user_cart = Cart.objects.get(user=request.user)  # Renamed the variable to user_cart
    user_cart.product.remove(product)
    return redirect("cart")