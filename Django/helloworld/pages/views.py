from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django import forms
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Sofia Mendieta",
        })
        return context
    
class Product:
 products = [
 {"id":"1", "name":"TV", "description":"Best TV", "price":10},
 {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":2000000},
 {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":3000000},
 {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":4000000}
 ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id)-1]
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse('creado'))
        return render(request, self.template_name, viewData)

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('creado.html')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
        return render(request, self.template_name, viewData)
    
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "title": "Contact us - Online Store",
        "subtitle": "Contact us",
        "email": "pepito@gmail.com",
        "address": "Calle 8A #10sur",
        "phonenumber": "3000000000",
        })
        return context

def creado(request):
    return render(request,"products/creado.html")

