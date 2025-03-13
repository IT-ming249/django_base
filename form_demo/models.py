from django.db import models
from django.core import validators
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100,validators=[validators.MinLengthValidator(limit_value=2)])
    content = models.TextField(validators=[validators.MinLengthValidator(limit_value=3)])
    create_time = models.DateTimeField(auto_now_add=True) #指定auto_now_add=True 表单验证时可不写
    category = models.CharField(max_length=100) #指定表单验证时可为空blank=True，数据库为空则null=True