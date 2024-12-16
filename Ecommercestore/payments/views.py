from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse


import io
from django.http import FileResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from payments.models import Payment
from store.models import Cart,Product

## for testing
def paymenttest(request):
    return HttpResponse(" payment app is connected")


# payment/views.py



## pdf generation library
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Function to generate bill
def generate_pdf_bill(user, total_amount, products):
    # Debug print
    print(f"User: {user}, Total Amount: {total_amount}, Products: {products}")

    # Create an HTTP response with PDF content type
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="bill_slip.pdf"'

    # Create the PDF using ReportLab
    p = canvas.Canvas(response)
    p.drawString(100, 800, f"User: {user.username}")
    p.drawString(100, 780, f"Total Amount: ${total_amount}")
    p.drawString(100, 760, "Products:")
    y = 740
    for product in products:
        p.drawString(120, y, f"- {product.name}: ${product.price}")
        y -= 20
    p.showPage()
    p.save()

    # Return the response for download
    return response



# Checkout view
@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    total_amount = sum(product.price for product in cart.product.all())

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method', 'PayPal')

        # Get the products for the bill BEFORE clearing the cart
        products = list(cart.product.all())

        # Create payment record
        payment = Payment.objects.create(
            user=request.user,
            total_amount=total_amount,
            payment_method=payment_method,
            payment_status='Pending',  # Can be updated after payment confirmation
        )
        payment.product.set(products)  # Associate products with payment

        # Clear the cart after products have been retrieved
        cart.product.clear()

        # Generate and return the PDF bill
        return generate_pdf_bill(request.user, total_amount, products)

    return render(request, 'payments/checkout.html', {'cart': cart, 'total_amount': total_amount})
    print("ok")

# Payment success view
@login_required
def payment_success(request):
    return render(request, 'payments/paymentsuccess.html')





