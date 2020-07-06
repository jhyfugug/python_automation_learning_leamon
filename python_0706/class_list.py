#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/6 23:54  
# @File   ：class_list.py

# 列表 list 符号[]
a = []
# 1: 可以存在空列表 a = []
a = [1, 0.02, 'hello', [1, 2, 3], True]
# 2：列表里面可以包含任何类型的数据
# 3:列表里面的元素  根据逗号来进行分隔
# 4:列表里面的元素 也是有索引的  索引值从0开始
# 5:列表的切片 同字符串的切片  列表头[索引头：索引尾：步长]
print(len(a))
print(a[-1])
print(a[0:5:2])     # 0 2 4

# 我们什么时候才用列表？
# 1:存储数据
# 2:如果你要存储的数据 是同一个类型  我们建议用列表

# 如何往列表追加数据    可以添加任意类型的数据
# append    追加    追加到末尾    只能追加一个数据
a.append("jhyfugug")
print("a列表的值{0}".format(a))

# insert  插入数据  想放哪就放哪  但是要指定位置--指定元素的索引值
a.insert(2, "monica")
print("a列表的值{0}".format(a))

# 删除  pop()   默认删除最后一个元素
# 删除  remove()   删除指定的值
# a.pop()
a.remove('monica')
res = a.pop()   # pop函数  会返回被删除的那个元素   函数return关键字
print("a列表的值{0}".format(a))

# 修改
a[4] = "wy"   # 赋值语句
print("a列表的值{0}".format(a))