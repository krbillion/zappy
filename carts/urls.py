from django.urls import path

from . import views

app_name='carts'

urlpatterns = [
    path('', views.view, name='cart'),
    path('<slug>', views.update_cart, name='update_cart'),
]
