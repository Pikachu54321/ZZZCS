from django.shortcuts import render, redirect
from app01 import models
from django.core.validators import RegexValidator
from django import forms
from django.utils.safestring import mark_safe
from app01.utils.pagination import Pagination
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.form import UserModelForm, PrettyModelForm, PrettyModelForm



def classification_list(request):
    """ 分类列表 """

    # 去数据库中获取所有的部门列表
    #  [对象,对象,对象]
    queryset = models.Classification.objects.all()
    page_object = Pagination(request, queryset, page_size=20)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }

    return render(request, 'classification_list.html', context)


def classification_add(request):
    """ 添加分类 """
    if request.method == "GET":
        return render(request, 'classification_add.html')

    # 获取用户POST提交过来的数据（title输入为空）
    title = request.POST.get("title")

    # 保存到数据库
    models.Classification.objects.create(title=title)

    # 重定向回部门列表
    return redirect("/classification/list/")




def classification_delete(request):
    """ 删除分类 """
    # 获取ID http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')

    # 删除
    models.Classification.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/classification/list/")


def classification_edit(request, nid):
    """ 修改分类 """
    if request.method == "GET":
        # 根据nid，获取他的数据 [obj,]
        row_object = models.Classification.objects.filter(id=nid).first()
        return render(request, 'classification_edit.html', {"row_object": row_object})

    # 获取用户提交的标题
    title = request.POST.get("title")

    # 根据ID找到数据库中的数据并进行更新
    # models.Department.objects.filter(id=nid).update(title=title,其他=123)
    models.Classification.objects.filter(id=nid).update(title=title)

    # 重定向回部门列表
    return redirect("/classification/list/")