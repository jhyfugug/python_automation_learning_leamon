#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/19 18:05  
# @File   ：do_file.py

# file   txt  xml  html

'''
file = open("python13.txt")
# mode   mode have a lit the way that open this file
# r   w   a    read  write  append
# r+    w+   a+
# rb rb+  wb  wb+  ab  ab+
res = file.read()
print(res)
'''

# file文件open之后默认是r   只读模式
# r+   可读可写    和光标有关系    先写就是从头开始覆盖
# 当写入中文的时候，需要注意编码格式
# W    可写
# W+   可读可写    不管是w还是w+，如果文件存在，那么文件内容会被清空，否则就是新建
# a  追加   如果文件存在，则直接追加写  写在后面   如果不存在，则创建一个文件进行记过写入

# file = open("python13.txt", "r+", encoding="utf-8")
# file.write("卡卡")
# res = file.read()
# print(res)

file = open("python13.txt", "a", encoding="utf-8")
# file.write("12133")
file.read()     # 读取所有内容
file.readline()     # 读取一行
file.readlines()        # 读取多行   返回的是列表