import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

import django

django.setup()

from app02 import models

ret = models.User.objects.filter(pk=2)
ret = models.User.objects.filter(pk__gt=2)  # > 2
ret = models.User.objects.filter(pk__gte=2)  # >=2
ret = models.User.objects.filter(pk__lt=2) # < 2
ret = models.User.objects.filter(pk__lte=2)  # <=2

ret = models.User.objects.filter(pk__in=[1,3])   #成员判断
ret = models.User.objects.filter(pk__range=[1,3])   # 范围判断，双侧闭合


ret = models.User.objects.filter(name__contains='wangyibo')   # like
ret = models.User.objects.filter(name__icontains='WANGYIBO')   # 忽略大小写


ret = models.User.objects.filter(name__startswith='wang')   # 以...开头
ret = models.User.objects.filter(name__istartswith='Wang')   # 以...开头 忽略大小写

ret = models.User.objects.filter(name__endswith='521')   # 以...结尾
ret = models.User.objects.filter(name__iendswith='EX')


ret = models.User.objects.filter(age__isnull=False) # age字段是否为空

ret = models.User.objects.filter(birth__year='2020')

ret = models.User.objects.filter(birth__contains='2020-06-05')
print(ret)


