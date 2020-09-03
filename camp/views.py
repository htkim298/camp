from django.shortcuts import render
from camp.models import SolViewData, SolData, Main
from django.views import View
from camp.models import SolData
from django.views.generic import TemplateView, ListView
from django.db.models import Sum
from django.db.models import Count, OuterRef, Subquery,Case, When, IntegerField,Value, DecimalField, BooleanField, Value


class ArticleListView(TemplateView):
    template_name = 'camp/index.html'

class GanwonArticleListView(ListView):
    template_name = 'camp/ganwonindex.html'

    context_object_name = 'asite_list' # 디폴트 컨텍스트 변수명 :  object_list
    def get_queryset(self): # 컨텍스트 오버라이딩
      return SolViewData.objects.aggregate(asite=Sum('asite')).values()

    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super().get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['bsite_list'] = SolViewData.objects.aggregate(asite=Sum('bsite')).values()
        context['csite_list'] = SolViewData.objects.aggregate(asite=Sum('csite')).values()
        context['dsite_list'] = SolViewData.objects.aggregate(asite=Sum('dsite')).values()
        context['esite_list'] = SolViewData.objects.aggregate(asite=Sum('esite')).values()
        context['day_list'] = SolViewData.objects.filter(cametc__in=['주중요금','중요금'] ).values('cametc').aggregate(asite=Sum('asite')+Sum('bsite')+Sum('csite')+Sum('dsite')+Sum('esite')).values()
        context['week_list'] = SolViewData.objects.filter(cametc__in=['주말요금','주요금'] ).values('cametc').aggregate(asite=Sum('asite')+Sum('bsite')+Sum('csite')+Sum('dsite')+Sum('esite')).values()
        return context

def post_list(request):
    posts = SolViewData.objects.all()
    return render(request, 'camp/post_list.html', {'posts': posts})
