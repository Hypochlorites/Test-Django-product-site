from django.shortcuts import render
from .models import Product


def homepage(request):
  context ={}
  return render(request, 'base/homepage.html', context)


def product(request):
  products = Product.objects
  context = {
    'products': products,
  }
  return render(request, 'base/product.html', context)
  

def mission(request):
  context = {}
  return render(request, 'base/mission.html', context)