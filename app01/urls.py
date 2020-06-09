from django.conf.urls import url
from app01 import views

urlpatterns = [
    # 展示出版社
    url(r'^publisher_list/$',views.publisher_list,name='publisher'),
    # 增加出版社
    url(r'^publisher_add/$',views.PublisherAdd.as_view(),name='pub_add'),
    # 删除出版社
    # url(r'^publisher_del/(\d+)/$',views.publisher_del,name='pub_del'),   # 将要删除的出版社id通过位置参数传递给视图函数publisher_del
    # 编辑出版社
    url(r'^publisher_edit/(?P<id>\d+)/$',views.publisher_edit,name='pub_edit'),   # 将要编辑的出版社id通过关键字参数传递给视图函数publisher_edit

    # 查看所有的图书
    url(r'^book_list/$',views.book_list,name='book'),

    # 添加图书
    url(r'^book_add/$',views.BookAdd.as_view(),name='book_add'),

    # 编辑图书
    url(r'^book/edit/(\d+)/',views.BookEdit.as_view(),name='book_edit'),

    # 删除图书
    # url(r'^book/del/(?P<pk>\d+)',views.book_del,name='book_del'),

    # 删除出版社和删除图书的逻辑一样，将url进行合并
    url(r'^(\w+)/del/(\d+)/',views.delete,name='del'),     # 按照位置参数传递给视图函数

    # 作者展示
    url(r'^author/$',views.author_list,name='author'),

    # 添加作者
    url(r'^author/add/$',views.author_add,name='author_add'),

    # 编辑
    url(r'^author/edit/(\d+)',views.author_edit,name='author_edit'),

]