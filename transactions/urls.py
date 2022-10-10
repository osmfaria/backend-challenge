from django.urls import path
from . import views

urlpatterns = [
    path('transactions/<str:store_name>/',views.retrieve_transactions, name="transactions"),
    path('search_stores/', views.search_stores, name='search-stores')
]