from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.products,name="product"),
    path('customers/<str:eli>/', views.customers,name="customer"),
    path('create_order/<str:pk>/',views.createOrder,name = "create_order"),
    path('update_order/<str:pk>/',views.updateOrder,name = "update_order"),
    path('delete_order/<str:pk>/',views.deleteOrder,name = "delete_order"), 
]