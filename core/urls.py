from django.urls import path
from . import views


urlpatterns = [
    # path('ship/',ShipList.as_view()),
    path("api/CartList/", views.ShipCarterList.as_view()),
    path("api/ShipList/", views.ShipList.as_view()),
    path("api/OwnerList/", views.OwnerList.as_view()),
]
