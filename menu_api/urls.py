from django.urls import path

from . import views
from menu_api import views as menu_views

urlpatterns = [
    path('', menu_views.add_menu),
    path('list/', menu_views.get_menu_list),
    path('list/<int:menu_id>/', menu_views.get_menu_by_id),
]