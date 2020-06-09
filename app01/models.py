from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=32)

    # __str__方法的作用:当打印对象时,打印的是__str__方法的返回值
    # __repr__方法与__str__不同：当打印对象时,首先检查该对象是否存在__str__方法,如果没有，再查找父类的__str__方法,最后再查找当前类的__repr__方法
    def __str__(self):
        return self.name

    __repr__ = __str__


class Book(models.Model):
    title = models.CharField(max_length=32)
    # 外键：django默认会加_id
    # 书籍和出版社的关系: 1个出版社可以出版多本书
    pub = models.ForeignKey('Publisher',on_delete=models.CASCADE)    # CASCADE : 级联删除 django2.0版本后on_delete参数是必填的
    # pub_id = models.ForeignKey('Publisher',on_delete=models.SET('1'))
    # pub_id = models.ForeignKey('Publisher',default=2,on_delete=models.SET_DEFAULT)
    # pub_id = models.ForeignKey('Publisher',null=True,on_delete=models.SET_NULL)
    # pub_id = models.ForeignKey('Publisher',on_delete=models.DO_NOTHING)
    # pub_id = models.ForeignKey('Publisher',on_delete=models.PROTECT)


class Author(models.Model):
    name = models.CharField(max_length=32)
    # 作者和书的关系   多对多的关系
    # 1. 一个作者  ---->  多本书
    # 2. 一本书 -----> 多个作者
    books = models.ManyToManyField('Book')  # 这个属性不会生成字段，但是会生成第三张表

    def show_books(self):
        return ",".join(["《{}》".format(book.title) for book in self.books.all()])

    