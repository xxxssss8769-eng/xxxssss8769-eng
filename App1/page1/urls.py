from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name='index1'),
    path('products/', views.products, name='Prods'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/', views.product, name='Prod'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('products/new/', views.new_cars, name='new_cars'),
    path('products/hire/', views.hire_cars, name='hire_cars'),
]