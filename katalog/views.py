from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def catalog_display(request):
    data_item_catalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_item_catalog,
        'name': 'Ammar Ash Shiddiq',
        'npm': '2106656560'
    }
    return render(request, 'katalog.html', context)