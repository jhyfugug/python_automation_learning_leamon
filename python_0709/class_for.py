#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/9 22:14  
# @File   ：class_for.py

# 循环  for   while
# python  for usage：
# for item in somedatetype: （数据类型包含： 字符串、列表、元组、字典、集合等）
# code block

# s = 'hello'
# l = [1, 2, 3]
# d = {"age": 20, "name": "jhyfugug"}
#
# for item in s:
#     print(item)
# from random import randint
#
# s = randint(1, 3)
# for x in range(1, 10):
#     print(s)
#
# x = 0
# for s in range(1, 101):
#     x = x + s
# print(x)

s = ""
q = int(input("请输入数字："))
for a in range(q):
    for b in range(1):
        s = s + "*"
        print(s)
