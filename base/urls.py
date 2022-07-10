from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homepage, name='home'),
    path('product', views.ProductListView.as_view(), name='product'),
    path('contact', views.contact, name='contact'),
    path('details/<int:pk>/', views.ProductDetailView.as_view(), name='details'),
    path('order/', views.createOrder, name='order'),
    path('orders', views.OrderListView.as_view(), name='orders'),
    path('fulfillmentation/<int:pk>/', views.OrderUpdateView.as_view(), name='fulfillmentation'),
    path('login', views.login, name='login'),
    # path('registration', views.Registration.as_view(), name='registration'),
]