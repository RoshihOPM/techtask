from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import MenuItem
from django.utils.text import slugify
# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class MenuItemDetailView(View):
    def get(self, request, url):
        menu_item = MenuItem.objects.get(url=url)
        return render(request, 'index.html', {'menu_item': menu_item})
