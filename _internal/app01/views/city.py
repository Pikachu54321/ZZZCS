from django.shortcuts import render, redirect
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.form import CityModelForm


def city_list(request):
    queryset = models.City.objects.all()
    for obj in queryset:
        print(obj.img)
    return render(request, 'city_list.html', {'queryset': queryset})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = "__all__"


def city_add(request):
    title = "新建单据"

    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_form.html', {"form": form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    print(request.FILES)
    if form.is_valid():
        # 对于文件：自动保存；
        # 字段 + 上传路径写入到数据库
        form.save()
        return redirect("/city/list/")
    return render(request, 'upload_form.html', {"form": form, 'title': title})


def city_edit(request, nid):
    """ 编辑单据 """
    row_object = models.City.objects.filter(id=nid).first()

    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据（对象）
        form = CityModelForm(instance=row_object)
        return render(request, 'upload_form.html', {'form': form})

    row_object.name = request.POST['name']
    row_object.count = request.POST['count']
    print(request.FILES)
    if 'img' in request.FILES:
        row_object.img = request.FILES['img']
    row_object.save()
    return redirect('/city/list/')


def city_delete(request, nid):
    models.City.objects.filter(id=nid).delete()
    return redirect('/city/list/')
