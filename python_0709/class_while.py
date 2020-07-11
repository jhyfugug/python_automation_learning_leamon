#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/9 23:46  
# @File   ：class_while.py

# while
# usage
# while expression:
#   code block

# 执行规律： 首先判断while后面的条件表达式是否成立
# 如果为True，那就执行code block，执行完毕之后再进行判断
# else, not access code block
#  avoid code going to endless loop: add a variable control cycles

# name = ["huahua", "ta", "pipi", "kaka"]
#
# username = input("请输入你的名字： \n")
# if username in name:
#     print("ok")

# while True:
#     print("1")
#     break

s = 0
while s < 10:
    s = s + 1
    print(s)