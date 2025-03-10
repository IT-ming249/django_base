from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    author = models.CharField(max_length=20,null=False)
    pub_time = models.DateTimeField(auto_now_add=True) #自动获取当前时间并赋值
    price = models.FloatField(default=0)                    #浮点类型

    #配置Meta (固定写法)
    class Meta:
        db_table = 'book_table' #指定表名字
        ordering = ['-pub_time','price']#指定排序方式，可多个，前一个相同则采用后一个排序


#常用Field演示
class Author(models.Model):
    is_active = models.BooleanField(default=True)           #bool类型
    name = models.CharField(max_length=200,null=False)      #字符串类
    date_joined = models.DateTimeField(auto_now_add=True)   #date类型
    email = models.EmailField(null=False)                   #邮箱类型 本质上是charfield
    visit_count = models.IntegerField(default=0)            #整型
    profile = models.TextField()                            #大量文本类型
    website = models.URLField()                             #网址类型

#Field常用参数演示
class Tag(models.Model):
    name = models.CharField(max_length=200,db_column="author_name",unique=True) #db_column指定表中列名
    #default 默认值，不支持lambda表达式 ,unique=True表示唯一
