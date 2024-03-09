from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('/',views.home,name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('menu/', views.menu, name='menu'),
    path('cart/',views.cart,name='cart'),
    path('BurgersAhoy!/',views.res1,name='res1'),
    path('CoffeeCrew/',views.res2,name='res2'),
    path('VintageBakery/',views.res3,name='res3'),
    path('RoyalRaso/',views.res4,name='res4'),
    path('TheVanillaBean/',views.res5,name='res5'),
    path('PureJuiceCo/',views.res6,name='res6'),
    path('CoffeeCrew/cart/', views.res2cart, name='res2cart'),
    path('BurgersAhoy!/cart/', views.res1cart, name='res1cart'),
    path('VintageBakery/cart/',views.res3cart,name='res3cart'),
    path('RoyalRaso/cart/', views.res4cart, name='res4cart'),
    path('TheVanillaBean/cart/', views.res5cart, name='res5cart'),
    path('PureJuiceCo/cart/', views.res6cart, name='res6cart'),


]
