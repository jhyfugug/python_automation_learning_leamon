#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/13 21:20  
# @File   ：class_function.py

# python 试错函数
# print input len type str int float list range
# pop append insert keys split replace strip
# remove clear

# 总结函数的特点：
# ①可以放使用

# 函数的语法： def staticword
# functionbody


# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)

# def add_numebrs(m, n, k=1):
#     sum = 0
#     for i in range(m, n, k):
#         sum = sum + i
#     return sum
#
# print(add_numebrs(1, 101))

# 默认参数  默认参数必须放在位置参数后面
def add_num(n, m=1, k=2):  # 位置参数/默认参数（都是形参）
    sum = 0
    for i in range(m, n, k):
        sum += i
    # print("最后的结果为：{0}".format(sum))
    return sum

print(add_num(10))   # 实参

