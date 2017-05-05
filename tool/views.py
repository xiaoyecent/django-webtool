# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from tool import ipapi
from tool import dic_generate

from django.shortcuts import render

# Create your views here.

def ip_api(request):
	#ip = request.GET['ipval']
	ip = request.GET.get('ipval', '')
	c, px, py = ipapi.ipapi(ip)
	ima = ipapi.getmap(px, py)
	return render(request, 'tool/ip.html', {'city':c,'px':px,'py':py,'ima':ima})
	
def dic(request):
	url = request.POST.get('url', '')
	url_dics = dic_generate.url_split(url)
	dic_final = dic_generate.dic_create(url_dics)
	return render(request, 'tool/dic.html', locals())