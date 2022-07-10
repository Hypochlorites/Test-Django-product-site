from django.shortcuts import render, redirect
from .models import Product
from .models import Order
from .forms import OrderForm, Registration
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def homepage(request):
  context ={}
  return render(request, 'base/homepage.html', context)

  
class ProductListView(ListView):
  model = Product 
  template_name = 'base/product.html' 
  
  

def contact(request):
  context = {}
  return render(request, 'base/contact.html', context)


# def fulfillmentation(request):
#   orders = Order.objects
#   context = {
#     "orders": orders,
#   }
#   return render(request, 'base/fulfillmentation.html', context)

class OrderUpdateView(UpdateView):
  model = Order
  fields = ['ordered_product', 'fulfillment_status']
  template_name = 'base/fulfillmentation.html'
  
class OrderListView(ListView):
  model = Order
  template_name = 'base/orders.html'







  

def login(request):
  context = {}
  return render(request, 'base/login.html', context)


class ProductDetailView(DetailView):
  model = Product
  template_name = 'base/details.html'

#Nightmare garbage



# @csrf_exempt
# def registration(request):
#   if request.method == 'POST':
#     form = Registration(request.POST)
#     if form.is_valid():
#       print("form valid")
#       form.save()
#       login(request, user)
#       return redirect('base/homepage.html')
      
#   else: 
#     form = Registration()
#     context = {'form': form}
#     return render(request, 'base/registration.html', context)

# @csrf_exempt
# class Registration(CreateView):
#   form_class = UserCreationForm
#   sucess_url = 'base/homepage.html'
#   template_name = 'base/registration.html/'
















  
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

  