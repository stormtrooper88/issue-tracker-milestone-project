from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Features

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "featuress.html", {"products": products})