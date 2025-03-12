from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class UserExtension(models.Model):
    birthday = models.DateField(null=True)
    school = models.CharField(max_length=50)
    user = models.OneToOneField("User", on_delete=models.CASCADE) #一对一限制的外键OneToOneField

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField("Tag", related_name="articles")#多对多限制的外键ManyToManyField(本质上是定义了一个中间表)
    #定义外键
    author = models.ForeignKey("User", on_delete=models.CASCADE,related_name="articles") #外键 级联
    #在已有数据的情况下添加新的列，需要设置null=True或默认值↓
    pub_time = models.DateTimeField(auto_now_add=True, null=True)
class Tag(models.Model):
    name = models.CharField(max_length=20)

"""
如果想引用另外一个app的模型作为外键，传递to参数的时候，使用app名进行指定
models.ForeignKey("user.User", on_delete=models.CASCADE) 表示绑定user这个app中的User作为外键
外键的删除操作(仅限Django层面，数据库级别依旧是RESTRICT)
CASCADE 级联
PROTECT 受保护
SET_NULL 设置为空，前提要设置null=True
SET_DEFAULT 设置默认值 前提要指定default = 值
SET()  SET()接受一个函数或对象，返回函数或对象的返回值
DO_NOTING 不采取任何行为
"""

class Comment(models.Model):
    content = models.TextField()
    #引用自身为外键↓
    origin_content = models.ForeignKey("self", on_delete=models.CASCADE,null=True)

