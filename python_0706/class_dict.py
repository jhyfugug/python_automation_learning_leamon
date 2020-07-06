#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/7 0:36  
# @File   ：class_dict.py

# 字典 dict  符号 {}
# 1: 可以存在空字典 a = {}
# 2: 字典里面数据存储方式   key：value
# 3：元组里面value可以包含任何类型的数据
# 4: 元组里面的元素  根据逗号来进行分隔

a = {"joy": "男", "haha": "女", "age": 20, "score": [80, 60]}
print(a)

# 字典取值：  字典[key]
print(a["score"])
# 字典删除：  pop（key）  # 指明删除的key
res = a.pop("age") # pop() 函数会返回删除值   return
print(res)
print(a)

# 新增   a[新key] = value
a["name"] = "jhyfugug"
print(a)

# 修改   a[已经存在的key] = 新value  字典中已存在的key
a["name"] = "wy"
print(a)

# 字典里面的key是唯一的
