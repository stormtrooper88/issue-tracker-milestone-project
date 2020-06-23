from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Features

# Create your views here.
def all_features(request):
    Features = Features.objects.all()
    return render(request, "features.html", {"features": features})