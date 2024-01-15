from django.shortcuts import render, redirect
from app01 import models

from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm


def user_list(request):
    """ 用户管理--入库物资管理 """

    queryset = models.UserInfo.objects.filter(out_or_in='入库')

    page_object = Pagination(request, queryset, page_size=20)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'user_list.html', context)


import datetime


def user_paper(request):
    """ 根据时间查询入库物资管理 """
    date = request.GET.get('date')

    print("日期参数:", date)

    if date:
        date_list = date.split('-')
    else:
        # 获取当前日期和时间
        now = datetime.datetime.now()

        # 格式化为"yyyy-mm-dd"格式
        date = now.strftime("%Y-%m-%d")
        date_list = date.split('-')
        print("当前日期:", date)

    print("date_list[0]", date_list[0])
    print("date_list[1]", date_list[1])
    print("date_list[2]", date_list[2])
    queryset = models.UserInfo.objects.filter(create_time__year=date_list[0]).filter(
        create_time__month=date_list[1]).filter(create_time__day=date_list[2])

    page_object = Pagination(request, queryset, page_size=20)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "search_data": date

    }

    return render(request, 'user_paper_list.html', context)


def user_add(request):
    """ 添加用户（原始方式） """

    if request.method == "GET":
        context = {
            'classification_list': models.Classification.objects.all(),
            "depart_list": models.Department.objects.all(),

        }
        print(context)
        return render(request, 'user_add.html', context)

    # 获取用户提交的数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    mtime = request.POST.get('mtime')
    classification_id = request.POST.get('gd')
    depart_id = request.POST.get('dp')
    out_or_in = request.POST.get('outIn')


    # 添加到数据库中
    models.UserInfo.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=ctime, maintenance_time=mtime,
                                   classification_id=classification_id, depart_id=depart_id, out_or_in=out_or_in)

    # 返回到用户列表页面
    return redirect("/user/list/")


def user_model_form_add(request):
    """ 添加用户（ModelForm版本）"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})

    # 用户POST提交数据，数据校验。
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        # {'name': '123', 'password': '123', 'age': 11, 'account': Decimal('0'), 'create_time': datetime.datetime(2011, 11, 11, 0, 0, tzinfo=<UTC>), 'gender': 1, 'depart': <Department: IT运维部门>}
        # print(form.cleaned_data)
        # models.UserInfo.objects.create(..)
        form.save()
        return redirect('/user/list/')

    # 校验失败（在页面上显示错误信息）
    return render(request, 'user_model_form_add.html', {"form": form})


def user_edit(request, nid):
    """ 编辑用户 """
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据（对象）
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要再用户输入以外增加一点值
        # form.instance.字段名 = 值
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {"form": form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
