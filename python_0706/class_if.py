#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/7 23:29  
# @File   ：class_if.py

# 控制语句  分支分流   循环语句   for  while

# 判断语句   if   elif   else
# if  条件语句（比较/逻辑/成员运算 均可）   空数据 = False   非空数据 = True
age = ' '
if age:
    print("恭喜你成年了！")

# if 条件语句
# else：     # 不能添加条件语句
# 子语句
age = 18

if age >= 18:
    print("成年了")
else:
    print("未成年")

# if  elif  else
if age > 18:
    print("1")
elif age == 18:
    print("2")
else:
    print("3")
