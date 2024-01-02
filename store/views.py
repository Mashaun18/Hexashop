from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, PaystackPayment
from django.contrib.auth.models import User
from .forms import PaymentForm
from django.contrib import messages
from django.conf import settings


def homepage(request):
    all_categories = Category.objects.all()
    male_products = Product.objects.filter(category=2)
    female_products = Product.objects.filter(category=1)
    context = {"all_categories": all_categories,
               "male_products": male_products,
               "female_products": female_products}
    return render(request, "store/index.html", context)


# from paystackapi.transaction import Transaction

# def verify_payment(ref):
#     transaction = Transaction.verify(ref)

#     if transaction:
#         save_payment_to_database()
#     else:
#         handle_failed_payment_verification()

# def save_payment_to_database():
#     # Save the payment to the database
#     pass

# def handle_failed_payment_verification():
#     # Handle failed payment verification
#     pass


def initiate_payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            paystack_public_key = settings.PAYSTACK_PUBLIC_KEY
            return render(
                request,
                'store/make_payment.html',
                {
                    'payment': payment,
                    'paystack_public_key': paystack_public_key,
                }
            )
    else:
        payment_form = PaymentForm()
    
    return render(
        request,
        "store/initiate_payment.html",
        {"payment_form": payment_form}
    )


def verify_payment(request, ref):
    payment = PaystackPayment.objects.get(reference=ref)
    verified = payment.verify_payment()
    
    message = "Verification Successful" if verified else "Verification Failed"
    messages.add_message(request, messages.SUCCESS if verified else messages.ERROR, message)
    
    return redirect("initiate_payment")
