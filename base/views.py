from django.shortcuts import render
from .models import Product
from .models import Order
from .forms import OrderForm
from django.views.decorators.csrf import csrf_exempt
import datetime

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

def contact(request):
  context = {}
  return render(request, 'base/contact.html', context)

def settings(request):
  context = {}
  return render(request, 'base/settings.html', context)

def fulfillmentation(request):
  orders = Order.objects
  context = {
    "orders": orders,
  }
  return render(request, 'base/fulfillmentation.html', context)








def details(request, pk):
  product = Product.objects.get(id = pk)
  context = {
    'product': product, 
  }
  return render(request, 'base/details.html', context)











  
@csrf_exempt
def createOrder(request):
  if request.method == "POST":
    filled_form = OrderForm(request.POST)
    if filled_form.is_valid(): 
      note = "Your order has been processed"
      new_form = OrderForm()
      context = {
        "orderform" : new_form,
        "note" : note
      }

      orderedproduct = request.POST["ordered_product"]
      firstname = request.POST["first_name"]
      lastname = request.POST["last_name"]
      address = request.POST["address"]
      city = request.POST["city"]
      zipcode = request.POST["zip_code"]
      time = datetime.datetime.now()
      
      
      new_order = Order(ordered_product = orderedproduct, first_name = firstname, last_name = lastname, address = address, city = city, zip_code = zipcode, order_time = time, fulfillment_status = False)
      
      new_order.save()
      return render(request, 'base/createOrder.html', context)

  else:
    form = OrderForm()
    context={
      "orderform" : form,
    }
    return render(request, 'base/createOrder.html', context)