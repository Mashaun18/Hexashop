from django.db import models
from .paystack import PayStack        
import secrets

class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=100)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return f"Payment {self.amount}"
    
    def amount_value(self):
        return self.amount * 100
    
    # def save(self, *args, **kwargs):
    #     while not self.ref:
    #         ref = secrets.token_urlsafe(50)
    #         if not Payment.objects.filter(ref=ref).exists():
    #             self.ref = ref
    #     super().save(*args, **kwargs)  


    def verify_payment(self):
        payment = PayStack()
        status, result = payment.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False          