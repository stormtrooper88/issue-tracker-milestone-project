from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Features
import datetime
from .forms import FeaturePostForm


# Create your views here.
def all_features(request):
    """
    Create a view that will return a list of all features that were published prior to 'now' and give them the 'featuress.html' template
    """
    features = Features.objects.all()
    form = FeaturePostForm(instance=None)
    return render(request, "features.html", {"features": features, 'form': form})

def feature_detail(request, pk):
    """
    Create a view that will return a single feature object based on the feature ID(pk) and render it to the 'featuredetail.html' template.
    """
    feature = get_object_or_404(Features, pk=pk)
    feature.save()
    return render(request, "featuredetail.html", {'feature': feature})

def create_or_edit_feature(request, pk=None):
    """
    Create a view that allows users to create or edit a feature depending if the feature ID is null or not
    """
    feature = get_object_or_404(Features, pk=pk) if pk else None
    if request.method == "POST":
        print("We've got a POST request coming through, a feature got submitted")
        form = FeaturePostForm(request.POST, request.FILES, instance=feature)
        print(f"the form is: {form}")
        if form.is_valid():
            print("the form is valid")
            feature = form.save(commit=False)
            feature.created_date = datetime.datetime.now()
            feature.save()
            cart = request.session.get('cart', {})
            print(f"The cart before: {cart}")
            print(f"Saved feature looks like this: {feature}, with pk of {feature.pk}")
            if feature.pk in cart:
                cart[feature.pk] = int(cart[feature.pk]) + 1
            else:
                cart[feature.pk] = cart.get(feature.pk, 1)
            print(f"The cart after: {cart} and the feature in it: {cart[feature.pk]}!")
            request.session['cart'] = cart 
            return redirect(feature_detail, feature.pk)
    else:
        form = FeaturePostForm(instance=feature)
    return render(request, 'trackerfeatureform.html', {'form': form})