from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Sum, Q, Value, F, ExpressionWrapper, DurationField, query
from app01.utils.pagination import Pagination
from datetime import timedelta
from django.db.models.functions import Extract
from django.db import connection


def chart_list(request):
    """ 数据统计页面 """
    queryset = models.UserInfo.objects.filter(out_or_in='入库',maintenance_time__lt=F('create_time') + timedelta(days=4))
    page_object = Pagination(request, queryset, page_size=20)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'chart_list.html', context)

def chart_index(request):
    """ 跳转统计页面 """
    return redirect("/chart/list/")


def chart_bar(request):
    # """ 构造柱状图的数据 """
    # # 数据可以去数据库中获取
    # legend = ["梁吉宁", "武沛齐"]
    # series_list = [
    #     {
    #         "name": '钢管',
    #         "type": 'bar',
    #         "data": [15, 20, 36, 10, 10, 10]
    #     },
    #
    # ]
    # x_axis = ['钢管', '螺丝', '扳手', '设备', '网线']
    #
    # result = {
    #     "status": True,
    #     "data": {
    #         'legend': legend,
    #         'series_list': series_list,
    #         'x_axis': x_axis,
    #     }
    # }
    # return JsonResponse(result)
    """ 构造柱状图的数据 """
    # 从数据库中获取数据

    top5 = models.UserInfo.objects.values('name').annotate(total=Sum('age')).order_by('-total')
    top5 = top5[:5]
    x_axis = []
    legend = []
    data = []
    for item in top5:
        x_axis.append(item['name'])
        data.append(item['total'])

    series_list = [
        {
            # "name": '钢管',
            "type": 'bar',
            "data": data
        },
    ]

    print(data)
    print(x_axis)
    result = {
        "status": True,
        "data": {
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def chart_pie(request):
    """ 构造饼图的数据 """

    db_data_list = [
        {"value": 2048, "name": 'IT部门'},
        {"value": 1735, "name": '运营'},
        {"value": 580, "name": '新媒体'},
    ]

    result = {
        "status": True,
        "data": db_data_list
    }
    return JsonResponse(result)


def chart_line(request):
    legend = ["上海", "广西"]
    series_list = [
        {
            "name": '上海',
            "type": 'line',
            "stack": 'Total',
            "data": [15, 20, 36, 10, 10, 10]
        },
        {
            "name": '广西',
            "type": 'line',
            "stack": 'Total',
            "data": [45, 10, 66, 40, 20, 50]
        }
    ]
    x_axis = ['1月', '2月', '4月', '5月', '6月', '7月']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def highcharts(request):
    """ highcharts示例 """

    return render(request, 'highcharts.html')


from django.forms import ModelForm, Form
from django import forms
from app01 import models


# class TTModelForm(Form):
#     name = forms.CharField(label="用户名")
#     ff = forms.FileField(label="文件")
#
#
# def tt(request):
#     if request.method == "GET":
#         form = TTModelForm()
#         return render(request, 'change.html', {"form": form})
#     form = TTModelForm(data=request.POST, files=request.FILES)
#     if form.is_valid():
#         print(form.cleaned_data)
#     return render(request, 'change.html', {"form": form})

class TTModelForm(ModelForm):
    class Meta:
        model = models.XX
        fields = "__all__"


def tt(request):
    instance = models.XX.objects.all().first()
    if request.method == "GET":
        form = TTModelForm(instance=instance)
        return render(request, 'tt.html', {"form": form})
    form = TTModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
    return render(request, 'tt.html', {"form": form})
