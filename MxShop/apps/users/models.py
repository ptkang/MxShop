# import 导入顺序: 标准库>第三方库>本地库
# 各import类型之间需要用空行隔开
# 应避免使用通配符进行import，即from xxx import *
# 像_all_ , _author_ , _version_ 等这样的模块级属性，应该放在文档字符串的后面，以及除from _future_ 之外的import表达式前面

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    '''
    用户
    '''
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class VerifyCode(models.Model):
    '''
    短信验证码
    一个model建议必须拥有设置3个字段：add_time, update_time, deleted
    为什么有deleted的原因是在很多项目中删除实际并未真正删除，只是做了一个deleted的标记状态
    '''
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
