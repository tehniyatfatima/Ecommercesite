from django.shortcuts import render

from django.http import HttpResponse

## test function
def test(request):
    return HttpResponse(" store app is connected")


from django.shortcuts import render, redirect
from .models import Category, Product, Cart, Wishlist
from payments.models import CartItem
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
    cart_items = CartItem.objects.filter(cart=cart)
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    context = {"cart_items": cart_items, "total_amount": total_amount}
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
    user_cart, _ = Cart.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
    if not created:
        cart_item.quantity += 1  # Increment the quantity
        cart_item.save()
    return redirect("cart")

@login_required
def increase_quantity(request, pk):
    product = Product.objects.get(pk=pk)
    user_cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=user_cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart")


# Remove from cart view
@login_required
def remove_from_cart(request, pk):
    product = Product.objects.get(pk=pk)
    user_cart, _ = Cart.objects.get_or_create(user=request.user)
    
    # Find the cart item
    cart_item = user_cart.cartitem_set.filter(product=product).first()
    
    if cart_item:
        if cart_item.quantity > 1:
            # Decrease the quantity
            cart_item.quantity -= 1
            cart_item.save()
        else:
            # If quantity is 1, remove the product
            cart_item.delete()
    
    return redirect("cart")
