from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from app01 import models
from django.views import View

# Create your views here.
# 展示所有的出版社信息

def publisher_list(request):
    # 查询所有的出版社对象
    all_pubs = models.Publisher.objects.all()
    # 返回一个页面
    return render(request,'publisher_list.html',{'all_pubs':all_pubs})


# FBV
# def publisher_add(request):
#     # 当请求方式为post时,获取提交的数据
#     if request.method == "POST":
#         pub_name = request.POST.get('pub_name')
#         # 校验的提交的数据,提交的数据不能为空
#         if not pub_name:
#             return render(request,'publisher_add.html',{'error':'提交的数据不能为空'})
#         # 校验数据是否有重复
#         if models.Publisher.objects.filter(name=pub_name):
#             return render(request,'publisher_add.html',{'error':'出版社已存在'})
#         # 插入数据库
#         ret = models.Publisher.objects.create(name=pub_name)
#         # print(ret,type(ret))
#         # 跳转到展示页面
#         return redirect(reverse('app01:pub_list'))
#
#     # 当请求方式为get时,返回页面
#     return render(request,'publisher_add.html')


# 将publisher_add改写为CBV方式
class PublisherAdd(View):
    def get(self,request):
        return render(request,'publisher_add.html')

    def post(self,request):
        pub_name = request.POST.get('pub_name')
        # 校验数据
        if not pub_name:
            return render(request,'publisher_add.html',{'error':'提交的数据不能为空'})
        if models.Publisher.objects.filter(name=pub_name):
            return render(request,'publisher_add.html',{'error':'该出版社已存在'})
        # 插入数据
        ret = models.Publisher.objects.create(name=pub_name)
        print(ret,type(ret))
        return redirect(reverse('app01:publisher'))



def publisher_del(request,pk):   # 通过url传递给视图函数，需要定义参数进行接收
    # # 获取提交的数据
    # pk = request.GET.get('pk')
    # 删除对应的数据
    models.Publisher.objects.get(pk=pk).delete()   # 删除单个对象
    # models.Publisher.objects.filter(pk=pk).delete()  # 对象列表删除
    # 跳转到展示页面
    return redirect(reverse('app01:publisher'))

def publisher_edit(request,id):    # 通过关键字参数传递,参数必须与分组命名一致
    # 获取要编辑的对象，先获取主键，再查询数据库获取对象
    # pk = request.GET.get('pk')
    obj = models.Publisher.objects.get(pk=id)    # get方法获取是单个对象,filter方法获取的是对象列表

    # 根据请求方法,如果请求方法为POST
    if request.method == "POST":
        # 获取提交的新数据
        pub_name = request.POST.get('pub_name')
        # 检验数据
        # 如果pub_name是空的:
        if not pub_name:
            return render(request,'publisher_add.html',{'error':'出版社名字不能为空'})
        # 如果出版社名字已存在
        if models.Publisher.objects.filter(name=pub_name):
            return render(request,'publisher_add.html',{'error':'该出版社已存在'})
        obj.name = pub_name  # 只是在内存中修改了obj对象的name属性
        obj.save()   # save方法将obj对象的修改保存到数据库中
        # 数据保存后,重定向到展示页面
        return redirect(reverse('app01:publisher'))    # 最好不用使用render,会造成页面和访问的url不一致
    # 如果请求方法为GET，则返回编辑界面
    return render(request,'publisher_edit.html',{'obj':obj})



def book_list(request):
    books = models.Book.objects.all()   # 获取的是对象列表[book_obj]
    # for book in books:
    #     print(book.id)
    #     print(book.title)
    #     print(book.pub,type(book.pub))    # book.pub(外键)  获取到的是Pulisher对象
    #     print(book.pub.name,book.pub.id,book.pub_id)    # 从数据库中获取所关联的对象id

    # return HttpResponse('ok')
    return render(request,'book_list.html',{'books':books})


class BookAdd(View):
    def get(self,request):
        # 查询所有的出版社
        all_pubs = models.Publisher.objects.all()
        return render(request,'book_add.html',{'all_pubs':all_pubs})

    def post(self,request):
        # 获取参数
        title = request.POST.get('title')
        pub_id = request.POST.get('pub_id')
        # 校验数据
        if not title:
            return render(request,'book_add.html',{'error':'书名不能为空'})
        if models.Book.objects.filter(title=title):
            return render(request,'book_add.html',{'error':'该书籍已存在'})
        # 插入数据
        # 方法1：使用pub，需要传递的是Publisher的对象
        # models.Book.objects.create(title=title,pub=models.Publisher.objects.get(pk=pub_id))
        # 方法2：使用pub_id，直接传递pub_id，建议的方式
        models.Book.objects.create(title=title,pub_id=pub_id)
        return redirect(reverse('app01:book'))


class BookEdit(View):
    def get(self,request,pk):
        book_obj = models.Book.objects.get(pk=pk)
        all_pubs = models.Publisher.objects.all()
        return render(request,'book_edit.html',{'book_obj':book_obj,'all_pubs':all_pubs})

    def post(self,request,pk):
        # book_obj = models.Book.objects.get(pk=pk)
        # 获取新提交的数据
        title = request.POST.get('title')
        pub_id = request.POST.get('pub_id')

        # 校验数据(title)
        if not title:
            # 如果title为空
            return render(request,'book_edit.html',{'error':'书籍名不能为空'})
        if models.Book.objects.filter(title=title):
            # 如果图书名字已存在
            return render(request,'book_edit.html',{'error':'该书名已存在'})
        # 修改方式1：
        # 修改
        # book_obj.title = title
        # book_obj.pub_id = pub_id
        # # book_obj.pub = models.Publisher.objects.get(pk=pub_id)
        # # 保存
        # book_obj.save()   # save会更新所有的字段，效率比较低

        # 修改方式2
        models.Book.objects.filter(pk=pk).update(title=title,pub_id=pub_id)

        return redirect(reverse('app01:book'))



def book_del(request,pk):
    models.Book.objects.get(pk=pk).delete()
    return redirect(reverse('app01:book'))


def delete(request,table,pk):
    # print(table,type(table),table.capitalize())
    # print(pk)
    # 使用反射获取到model的名字
    model_class = getattr(models,table.capitalize())
    # 删除条目
    model_class.objects.get(pk=pk).delete()
    # 此处重定向界面用url反向解析,需要修改url命名与table一致
    return redirect(reverse('app01:%s'%table))


def author_list(request):
    all_authors = models.Author.objects.all()
    # for author in all_authors:
    #     print(author.pk)
    #     print(author.name)
    #     print(author.books,type(author.books))   # 获取到的是关系管理对象 django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager
    #     print(author.books.all(),type(author.books.all()))   # 关联的所有对象
    return render(request,'author.html',{'all_authors':all_authors})


def author_add(request):
    if request.method == "POST":
        # 获取用户提交的数据
        author_name = request.POST.get('author_name')
        book_id = request.POST.getlist('book_id')
        # print(request.POST) #<QueryDict: {'csrfmiddlewaretoken': ['9p2MhTII9Av1FISFJdtl3vdLPRfDgNGJqdvgkGzoHwBhW79XXsFu6EJTXLf6sYKU'], 'author_name': ['肖战'], 'book_id': ['2', '3']}>
        # print(author_name)
        # print(book_id)  # 只取到了最后一个元素3,为了获取所有数据，需要使用getlist方法

        # 校验数据
        if not author_name:
            return render(request,'author_add.html',{'error':'作者名不能为空'})
        if models.Author.objects.filter(name=author_name):
            return render(request,'author_add.html',{'error':'该作者已存在'})

        # 插入数据
        author_obj = models.Author.objects.create(name=author_name)
        # 设置多对多关系
        author_obj.books.set(book_id)  # [2,3] 在第三张表中创建多对对关系

        # 重定向到作者展示页面
        return redirect(reverse("app01:author"))


    all_books = models.Book.objects.all()
    return render(request,'author_add.html',{'all_books':all_books})



def author_edit(request,pk):
    author_obj = models.Author.objects.get(pk=pk)
    all_books = models.Book.objects.all()
    if request.method == "POST":
        # 获取新提交的数据
        author_name = request.POST.get('author_name')
        book_id = request.POST.getlist('book_id')
        # 校验数据(author_name不能为空)
        if not author_name:
            return render(request,'author_add.html',{'error':'作者名不能为空'})
        author_obj.name = author_name
        author_obj.save()
        author_obj.books.set(book_id)
        return redirect(reverse('app01:author'))

    # all_books = models.Book.objects.all()
    return render(request,'author_edit.html',{'author_obj':author_obj,'all_books':all_books})



