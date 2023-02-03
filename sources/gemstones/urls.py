from django.urls import path, re_path

from . import views


urlpatterns = [
    path('add_deal', views.add_deal, name='add_deal'),
    path('find_top_five_clients', views.find_top_five_clients, name='find_top_five_clients'),
]
