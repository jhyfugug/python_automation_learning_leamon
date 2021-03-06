#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/7 0:16  
# @File   ：class_tuple.py

# 元组  tuple  符号 （）
a = (1, 0.02, 'hello', [1, 2, 3], True, (4, 5, 6))

# 1: 可以存在空元组 a = （）
# 2：元组里面可以包含任何类型的数据
# 3:元组里面的元素  根据逗号来进行分隔
# 4:元组里面的元素 也是有索引的  索引值从0开始
# 5:元组的切片 同字符串的切片  元组头[索引头：尾：步长]

# 元组的元素不可以修改（增删改）   一般用于操作数据的时候  存放条件
# a[3][-1] = 2    # 特殊情况   元组里面的列表整体不可修改，但是可以修改list里面的元素
# # a[5][-2] = 4    # 元组不可变更
# a[3].pop()
# print("a的数据为{0}".format(a))

a = (1)     # 如果你的元组里面只有一个元素的，请加逗号
print(type(a))

b = (1,)       # 这个才是元组
print(type(b))
