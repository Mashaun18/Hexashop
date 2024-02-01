from django.urls import path
from .views import homepage, detailpage, store_initiate_payment, ApiHomePage


urlpatterns = [
    path("", homepage),
    path("api/", ApiHomePage.as_view()),
    path("<int:id>/", detailpage, name="detailpage"),
    path("<int:id>/pay/", store_initiate_payment, name="store-initiate-payment"),
]