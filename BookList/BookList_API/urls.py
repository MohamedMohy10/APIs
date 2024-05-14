from django.urls import path
from . import views


urlpatterns = [
path('books', views.Books),
path('inventory', views.Inventory_Books)
]