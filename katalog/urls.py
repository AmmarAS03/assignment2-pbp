# TODO: Implement Routings Here
from django.urls import path
from katalog.views import catalog_display

app_name = 'katalog'

urlpatterns = [
    path('',catalog_display,name='show_catalog')
]