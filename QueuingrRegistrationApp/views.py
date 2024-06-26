import time

from django.shortcuts import render

# Create your views here.
import json
import time
# import simplejson
from datetime import datetime, timedelta
from django.shortcuts import render, HttpResponse
from django.views import View
from QueuingrRegistrationApp.api import get_mz_queue_data
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import jwt


class MzQueueView(View):
    def get(self, request):
        get_obj = {
            'search_type': request.GET.get('search_type'),
            'search_content': request.GET.get('search_content'),
        }
        paramObj = {
            '科室名称': '',
            '门诊号': '',
            '电话': '',
            '患者姓名': '',
            '医生姓名': ''
        }
        if get_obj['search_type']:
            paramObj[get_obj['search_type']] = get_obj['search_content']
        if request.GET.get('pageStart'):
            get_obj['pageStart'] = request.GET['pageStart']
        if request.GET.get('pagesize'):
            get_obj['pagesize'] = request.GET['pagesize']
        data = get_mz_queue_data(paramObj)
        data_set = data[
            slice(int(get_obj['pageStart']) * int(get_obj['pagesize']), (int(get_obj['pageStart']) + 1) * int(get_obj['pagesize']))]
        ret = dict(data=list(data_set))
        ret['message'] = 'success'
        ret['code'] = 20000
        ret['total'] = len(data)
        res = json.dumps(ret, cls=DjangoJSONEncoder)
        return HttpResponse(res, content_type='application/json')


class HomePage(View):
    def get(self, request):
        return render(request, 'index_queue.html')