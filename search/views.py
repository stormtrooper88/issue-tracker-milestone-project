from django.shortcuts import render
from bugs.models import Bug
from features.models import Features

# Create your views here.
def do_search(request):
    bugs = Bug.objects.filter(name__icontains=request.GET['q'])
    Features = Features.objects.filter(name__icontains=request.GET['q'])
    return render(request, "index.html", {"bugs": bugs, "features": features})