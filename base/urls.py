from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homepage, name='home'),
    path('product', views.product, name='product'),
    path('mission', views.mission, name='mission'),
    path('contact', views.contact, name='contact'),
    path('settings', views.settings, name='settings'),
    path('details/<int:pk>/', views.details, name='details'),
    path('order/', views.createOrder, name='order'),
    path('fulfillmentation', views.fulfillmentation, name='fulfillmentation')
]