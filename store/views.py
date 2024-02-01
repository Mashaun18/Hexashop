from django.shortcuts import render
from core.models import Payment
from .models import Category, Product
from django.contrib.auth.models import User
from django.conf import settings
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class ApiHomePage(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

def homepage(request):
    all_categories = cache.get("all_categories")
    male_products = cache.get("male_products")
    female_products = cache.get("female_products")
    if all_categories is None or male_products is None or female_products is None:
        all_categories = Category.objects.all()
        male_products = Product.objects.filter(category=2)
        female_products = Product.objects.filter(category=1)
        cache.set("all_categories", all_categories)
        cache.set("male_products", male_products)
        cache.set("female_products", female_products)
    context = {"all_categories": all_categories,
               "male_products": male_products,
               "female_products": female_products}
    return render(request, "store/index.html", context)


def detailpage(request, id):
    product = Product.objects.get(id=id)
    context = {"product": product}
    return render(request, "store/single-product.html", context)


def store_initiate_payment(request, id):
    product = Product.objects.get(id=id)
    email = request.user
    amount = product.price
    if request.method == 'POST':
        payment = Payment.objects.create(email=email, amount=amount)
        context = {
            "payment": payment,
            "product": product,
            "paystack_public_key": settings.PAYSTACK_PUBLIC_KEY
        }
        return render(request, "make_payment.html", context)
    context = {
        "product": product
    }
    return render(request, "store/initiate_payment.html", context)
    
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

