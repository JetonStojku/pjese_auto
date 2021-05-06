from django.shortcuts import render
from .models import Produkt
from auto.models import Marka

def index(request):
    return render(request, 'produkt/index.html')


def produkt(request):
    produkts = Produkt.objects.order_by('-serial')

    context = {
        'produkts': produkts,
    }
    return render(request, 'produkt/produkt.html', context)
