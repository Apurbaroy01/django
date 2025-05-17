from django.shortcuts import render
from .models import Product
from django.shortcuts import render
from .models import Product
from django.db.models import Q

def index(request):
    products = None
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            serial_number__exact=query
        )
    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'base/index.html', context)

