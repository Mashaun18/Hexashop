from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm
from django.contrib import messages
from .models import Payment
from django.conf import settings

def initiate_payment(request): 
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            paystack_public_key = settings.PAYSTACK_PUBLIC_KEY
            return render(request, 'core/make_payment.html', {'payment': payment, 'paystack_public_key': paystack_public_key,
                                                              'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})

    else:
        payment_form = PaymentForm()
    return render(request, "core/initiate_payment.html", {"payment_form": payment_form})


def verify_payment(request, ref):
    payment =get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Verification Successful")
    else:
        messages.error(request, "Verification Failed")
    return redirect("initiate_payment")
