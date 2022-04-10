from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homepage, name='home'),
    path('product', views.product, name='product'),
    path('mission', views.mission, name='mission'),
  
]