import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

import django

django.setup()

from app02 import models

#all()  获取所有的数据，结果是QuerySet [对象1.对象2...]
ret = models.User.objects.all()
print(ret)

#get() 获取一条数据  对象  缺点：查询不到或者有多条记录时会报错
ret = models.User.objects.get(pk=1)
print(ret)


#filter() 获取满足条件的所有数据  结果是:QuerySet
ret = models.User.objects.filter(pk=1)
print(ret)

#exclude()  获取不满足条件的所偶对象  QuerySet [对象1,对象2]
ret = models.User.objects.exclude(pk=1)
print(ret)

#order_by() 排序 QuerySet , 默认是升序
ret = models.User.objects.order_by('uid')
print(ret)
ret = models.User.objects.order_by('-uid')   # 按照降序排序
print(ret)

ret = models.User.objects.order_by('age','-uid')   #先按照age升序排序，再按uid降序排列
print(ret)


#reverse() 反转，对以排序的结果进行反转
ret = models.User.objects.all().order_by('uid').reverse()


#values()  QuerySet [字典,字典]  不加参数，获取所有的字典名和值
#values('uid','name')  指定参数,获取指定字段的名和值
ret = models.User.objects.all().values()
for r in ret:
    print(r['uid'],r['name'],r['age'],r['phone'],r['gender'])


#values_list()   不加参数，获取所有的字段值  QuerySet [(),()]
#values_list('name','uid')  # 获取指定字段的字段值 QuerySet [(),()]
ret = models.User.objects.all().values_list()
for r in ret:
    print(r)

ret = models.User.objects.all().values_list('age','name','phone')
for r in ret:
    print(r)


#distinct 去重
ret = models.User.objects.all().values('phone').distinct()
print(ret)

# first  取第一个元素，如果没有的话就是None
ret = models.User.objects.filter(name='wangyibo521').first()
print(ret)

# last 取最后一个元素,没有的话就是None
ret = models.User.objects.all().last()
print(ret)


# count 计数 len()  __len__  count比len的效率高
ret = models.User.objects.all().count()
print(ret)


# exists() 判断查询结果是否存在
ret = models.User.objects.filter(name='alex').exists()
print(ret)


"""
返回结果是QuerySet的：
1. all()
2. filter()
3. exclude()
4. order_by()
5. reverse()
6. values()
7. values_list()
8. distinct 

返回结果是对象的:
1. get()
2. first()
3. last()

返回数字的：
1. count()

返回布尔值:
1. exists()

"""