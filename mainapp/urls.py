from django.urls import path

from . import views

app_name='mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<slug>', views.detail, name='detail'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    # path('cart', views.cart, name='cart'),
    path('search/', views.search, name='search'),
    path('profile', views.profile, name='profile'),
]
