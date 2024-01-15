from django.shortcuts import render, redirect
from app01 import models

from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm, PrettyModelForm, PrettyModelForm


def out_list(request):
    """ 出库物资管理管理--入库物资管理 """
    queryset = models.UserInfo.objects.filter(out_or_in='出库')

    page_object = Pagination(request, queryset, page_size=20)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'user_list_out.html', context)


def out_add(request):
    """ 添加出库物资管理（原始方式） """

    if request.method == "GET":
        context = {
            'classification_list': models.Classification.objects.all(),
            "depart_list": models.Department.objects.all()
        }
        print(context)
        return render(request, 'user_add_out.html', context)

    # 获取出库物资管理提交的数据
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

    # 返回到出库物资管理列表页面
    return redirect("/out/list/")

def out_edit(request, nid):
    """ 编辑出库物资管理 """
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据（对象）
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit_out.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是出库物资管理输入的所有数据，如果想要再出库物资管理输入以外增加一点值
        # form.instance.字段名 = 值
        form.save()
        return redirect('/out/list/')
    return render(request, 'user_edit_out.html', {"form": form})


def out_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/out/list/')
