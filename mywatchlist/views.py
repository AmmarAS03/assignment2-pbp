from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.


def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
    'watch_list' : data_mywatchlist,
    'name' : 'Ammar Ash Shiddiq',
    'npm': '2106656560'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_html(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
    'watch_list' : data_mywatchlist,
    'name' : 'Ammar Ash Shiddiq',
    'npm': '2106656560'
    }
    return render(request, "mywatchlist.html", context)
