from django.urls import path
from . import views
from .views import ArticleListView


urlpatterns = [
    path('', ArticleListView.as_view()),
    path('solcamp/', views.post_list, name='post_list'),
]
