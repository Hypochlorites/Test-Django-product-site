from django import forms 



class OrderForm(forms.Form):
  ordered_product = forms.CharField(max_length=30)
  first_name = forms.CharField(max_length=20)
  last_name = forms.CharField(max_length=20)
  address = forms.CharField(max_length=50)
  city = forms.CharField(max_length=40)
  zip_code = forms.CharField(max_length=5)
  
  