from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('aa/', views.SearchListView.as_view(), name='index'),
]
