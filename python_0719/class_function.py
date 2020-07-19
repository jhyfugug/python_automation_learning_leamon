#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/19 15:57  
# @File   ：class_function.py

# variable scope

# a = 1  # Global variable
#
# def add(b):
#     a = 5  # Local variable
#     print(a + b)
#
# add(10)

# Global variable and Local variable
# 1: different scope  Global: call in the module.  Local: call in the function
# 2: When global variables and local variables exist at the same time and at the
# same name, local variables have higher priority than global variable
# 3: When where are no local variables, use global variables
# 4: global       global assignment

# previous period homework

num = input("请输入一个4位数：\n")
def four_num_conversion(num):
    add_5 = 0
    new_num = ""
    output_num = ""
    for item in num:
        # print(item)
        add_5 = int(item) + 5
        # print("每位数加5：", add_5)
        # print("每位数的取余后为：", add_5 % 10)
        new_num += str((int(item) + 5) % 10)
    output_num = new_num[::-1]
    return output_num

print(four_num_conversion(num))