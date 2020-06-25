from django.shortcuts import get_object_or_404
from features.models import Features

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    Features_count = 0

    for id, quantity in cart.items():
        Features = get_object_or_404(Product, pk=id)
        total += quantity * Features.price
        Features_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'Features': Features})

    return {'cart_items': cart_items, 'total': total, 'Features_count': Features_count}