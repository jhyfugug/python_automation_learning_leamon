#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/9 23:46  
# @File   ：class_while.py

# while
# name = ["huahua", "ta", "pipi", "kaka"]
#
# username = input("请输入你的名字： \n")
# if username in name:
#     print("ok")

# while True:
#     print("1")
#     break

# s = 0
# while s < 10:
#     s = s + 1
#     print(s)
#
# s = 0
# number = 0
# while number < 100:
#     number = number + 1
#     s = s + number
# print(s)




s = {"jhyfugug": "123"}
count = 3

while True:
    for name, pwd in s.items():
        input_name = input("请输入用户名：\n")
        if input_name == name:
            while count > 0:
                input_pwd = input("请输入密码：\n")
                if input_pwd == pwd:
                    print("登录成功！")
                    break
                else:
                    count = count - 1
                    print("你还有{}次机会输入密码".format(count))
        else:
            print("请输入正确的用户名：\n")
