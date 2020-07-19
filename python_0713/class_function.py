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
'''
# 默认参数  默认参数必须放在位置参数后面
def add_num(n, m=1, k=2):  # 位置参数/默认参数（都是形参）
    sum = 0
    for i in range(m, n, k):
        sum += i
    # print("最后的结果为：{0}".format(sum))
    return sum

print(add_num(10))   # 实参


def add_two(a, b):
    print(a + b)

add_two(1, 3)
# return 当你调用函数的时候，就会返回一个值 return 后面的表达式
# 在函数里面的return 相当于结束符号，表示函数到此为止

'''


# def check_list(L):
#     if len(L) > 2:
#         new_list = L[0:2]
#     return new_list
#
# B = [1, 2, 3, 4]
# print(check_list(B))

# 动态参数/不定长参数  args   arguments
# withdraw as a tuple in function
# def make_sandwich(*args):
#     # print("you's sandwich include {}".format(args))
#     all = ""
#     for item in args:
#         all += item
#         all += "、"
#     print("you’s sandwich include " + all)
#
# make_sandwich("生菜", "鸡蛋")

# 关键字参数   key-values    **kwargs   key word
# withdraw as a dictionary in function
# def kw_function(**kwargs):
#     print(kwargs)
#
# kw_function(k=1, y=2)

def add_all_num(a, *L, **kwargs):
    print(L)
    sum = 0
    for item in L:
        sum += item
    print("Totol is", sum)
    print(a)
    print(kwargs)


add_all_num(1, 2, 3, 4, 5, x=6, y=7)
