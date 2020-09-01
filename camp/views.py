from django.shortcuts import render
from camp.models import SolViewData, SolData
from django.views import View
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import os
from webdriver_manager.chrome import ChromeDriverManager
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webserver.settings")
import django
django.setup()
from camp.models import SolData


def post_list(request):
    posts = SolViewData.objects.all()
    return render(request, 'camp/post_list.html', {'posts': posts})


class SearchListView(View):
    def parse_blog(self):
        req = requests.get('https://camping.gtdc.or.kr/DZ_reservation/reserCamping.php?xch=reservation&xid=camping_reservation')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        my_titles = soup.select('tbody > tr > td')
        data = {}
        for title in my_titles:
            data[title.text] = title.get('')
        # data[title.text] = ". " + title.select_one("tr").get_text()
        return data

        blog_data_dict = parse_blog()
        for t, l in blog_data_dict.items():
            SolData(title=t).save()
