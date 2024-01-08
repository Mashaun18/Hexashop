from django.urls import path
from .views import homepage, detailpage, store_initiate_payment


urlpatterns = [
    path("", homepage),
    path("<int:id>/", detailpage, name="detailpage"),
    path("<int:id>/pay/", store_initiate_payment, name="store-initiate-payment")
]