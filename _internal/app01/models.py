from django.db import models


class XX(models.Model):
    title = models.CharField(verbose_name="名称", max_length=32)
    image = models.FileField(verbose_name="头像", upload_to="avatar/")


class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name='标题', max_length=32)

    def __str__(self):
        return self.title

class Classification(models.Model):
    """ 种类表 """
    title = models.CharField(verbose_name='标题', max_length=32)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """ 员工表 ---出入库表"""
    name = models.CharField(verbose_name="物资名称", max_length=16)
    password = models.CharField(verbose_name="物资编号", max_length=64)
    age = models.IntegerField(verbose_name="数量")
    account = models.DecimalField(verbose_name="长度", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name="出入库时间")
    depart = models.ForeignKey(verbose_name="物资供应商", to="Department", to_field="id", on_delete=models.CASCADE)
    classification = models.ForeignKey(verbose_name="状态", to="Classification", to_field="id", on_delete=models.CASCADE)
    maintenance_time = models.DateField(verbose_name="保养时间")
    out_or_in = models.CharField(verbose_name="出库或入库", max_length=16)



class StockInfo(models.Model):
    "---出入库表"""
    name = models.CharField(verbose_name="物资名称", max_length=16)
    create_time = models.DateField(verbose_name="出入库时间")
    maintenance_time = models.DateField(verbose_name="保养时间")

class PrettyNum(models.Model):
    """ 靓号表 """
    name = models.CharField(verbose_name="物资名称", max_length=50)
    mobile = models.CharField(verbose_name="物资编号", max_length=50)
    # 想要允许为空 null=True, blank=True
    price = models.IntegerField(verbose_name="数量", default=0)

    classification = models.ForeignKey(verbose_name="状态", to="Classification", to_field="id", on_delete=models.CASCADE)

    status_choices = (
        (1, "已到货"),
        (2, "未到货"),
        (3, "已出库"),
        (4, "未出库"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)
    # maintenance_time = models.DateField(verbose_name="保养时间")


class Task(models.Model):
    """ 任务 """
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")

    # user_id
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)


class Order(models.Model):
    """ 订单 """
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    status_choices = (
        (1, "已到货"),
        (2, "未到货"),
        (3, "已出库"),
        (4, "未出库"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)


    # admin_id
    admin = models.ForeignKey(verbose_name="管理员", to="Admin", on_delete=models.CASCADE)


class Boss(models.Model):
    """ 老板 """
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    img = models.CharField(verbose_name="头像", max_length=128)


class City(models.Model):
    """ 城市 """
    name = models.CharField(verbose_name="名称", max_length=32)
    count = models.CharField(verbose_name="单据编号",max_length=64)

    # 本质上数据库也是CharField，自动保存数据。
    img = models.ImageField(verbose_name="图片", max_length=128, upload_to='city/')
