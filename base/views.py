from django.shortcuts import render

def homepage(request):
  context ={}
  return render(request, 'base/homepage.html', context)


def product(request):
  context ={}
  return render(request, 'base/product.html', context)

def mission(request):
  context = {}
  return render(request, 'base/mission.html', context)