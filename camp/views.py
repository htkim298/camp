from django.shortcuts import render
from camp.models import SolViewData, SolData, Main
from django.views import View
from camp.models import SolData
from django.views.generic import TemplateView

class ArticleListView(TemplateView):         # 게시글 목록
    template_name = 'camp/index.html'

def post_list(request):
    posts = Main.objects.all()
    return render(request, 'camp/post_list.html', {'posts': posts})
