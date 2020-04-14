from django.urls import path

from . import views

urlpatterns = [
    path('', views.MenuList.as_view()),
    path('<int:pk>/', views.MenuDetail.as_view()),
]