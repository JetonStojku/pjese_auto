from django.shortcuts import render
from .models import Produkt
from auto.models import Marka

def index(request):
    return render(request, 'produkt/index.html')


def produkt(request):
    marka_emer = request.GET.get('marka')
    if marka_emer:
        produkts = Produkt.objects.filter(marka__emer__exact=marka_emer)
    else:
        produkts = Produkt.objects.all()
    # produkts = Produkt.objects.order_by('-serial')
    markat = Marka.objects.order_by('-emer')
    context = {
        'produkts': produkts,
        'markat': markat,
        'marka_emer': marka_emer
    }
    return render(request, 'produkt/produkt.html', context)
