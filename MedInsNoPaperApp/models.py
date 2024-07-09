from django.db import models


# Create your models here.
class UserInfo(models.Model):
    # 账号表
    account = models.CharField(verbose_name="账号", max_length=256)
    password = models.CharField(verbose_name="密码", max_length=256)
    name = models.CharField(verbose_name="姓名", max_length=256)
    permission_type = models.CharField(verbose_name="权限类型", max_length=256)
    detail_info = models.TextField(verbose_name="账号详情")

    def __str__(self):
        # 解决ModelForm的外键引用返回对象的问题.
        return self.account


class MedInsInfo(models.Model):
    # 医保档案表
    med_ins_info = models.TextField(verbose_name="医保详情")
    imgs = models.TextField(verbose_name="图片信息")

    def __str__(self):
        # 解决ModelForm的外键引用返回对象的问题.
        return self.med_ins_info


# 存放图片的表
# class Avatar(models.Model):
#     user = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='photos', default='avatar.jpg')