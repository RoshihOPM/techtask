from django.urls import path
from menu.views import IndexView, MenuItemDetailView


urlpatterns = [
    path('', IndexView.as_view()),
    path('menu/<str:url>/', MenuItemDetailView.as_view(), name='menu_item_detail'),
]
