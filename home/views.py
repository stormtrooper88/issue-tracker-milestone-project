from django.shortcuts import render

# Create your views here.
def front(request):
    """A loading page for users"""
    return render(request, "front.html")
