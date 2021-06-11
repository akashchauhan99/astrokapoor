from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('seller/', SellerView.as_view()),
    path('categoryservice/<int:pk>/', CategoryServiceView.as_view()),

    path('birth/', BirthView.as_view()),
    path('birth/<int:pk>/', BirthDetailView.as_view()),

    path('contactdetail/', ContactView.as_view()),
    path('contactdetail/<int:pk>/', ContactDetailView.as_view()),
]