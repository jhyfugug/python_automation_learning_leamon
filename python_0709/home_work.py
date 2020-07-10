#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/9 22:00  
# @File   ：home_work.py

'''
total = int(input("请输入购买金额:"))
if total < 50:
    print("你没法享受折扣")
    print("您需要支付{0}元".format(total))
elif 50 <= total <= 100:
    print("您将享受10%的折扣")
    print("您需要支付{0}元".format(total * (1 - 0.1)))
else:
    print("您将享受20%的折扣")
    print("您需要支付{0}元".format(total * (1 - 0.2)))
'''

from random import randint

x = randint(1, 9)
y = int(input("请输入你的数字："))

if y > x:
    print("bigger")
elif y < x:
    print("less")
else:
    print("equal")

print(x)