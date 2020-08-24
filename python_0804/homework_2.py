#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/8/19 7:49  
# @File   ：homework_2.py

# 贩卖机
drink = {"1": 1.5, "2": 2.5, "3": 2, "4": 4.5}
total = 0
while True:
    choose = input("请选择饮料：\n")
    if choose in drink.keys():
        total += drink[choose]
        print("您选择的酒水为{0}，而且总价为{1}".format(drink[choose], total))
    elif choose == "q":
        print("退出选择饮料")
        break
    else:
        print("你选择的饮料不存在，请重新选择")

solary = 0

while True:
    amt = input("请投币！")
    if amt == "1" or amt == "2" or amt == "5" or amt == "10":
        solary += int(amt)
        print("你本次投入的金额为{0}，总金额为{1}".format(amt, solary))
        if total < solary:
            print("你本次总计消费{0}元，找零{1}元，请收好你的饮料和零钱".format(total, solary - total))
            break
        elif total == solary:
            print("你本次总计消费{0}元,刚好足够支付".format(total))
        else:
            print("你的钱：{0}元 还不够支付当前选择的饮料：{1}元，还差：{2}元，请继续投币！".format(solary, total, total - solary))
    elif amt == "q":
        print("交易结束")
        break

    else:
        print("请投入正确的金币")
