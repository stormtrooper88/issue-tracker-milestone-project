from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Bug

# Create your views here.
def all_bugs(request):
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})