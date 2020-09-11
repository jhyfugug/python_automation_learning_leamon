#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/8/24 23:33  
# @File   ：classInstance_homework_1.py

class User:
    # 定义用户的方法类
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("该用户的第一个名字叫{0}，最后的名字叫{1}".format(self.first_name, self.last_name))

    def greet_user(self):
        print("Hi, {0}您好！，welcome to name 体验中心，你当前扮演的角色姓名是{1}，and "
              "your last name will change {2}".format(self.first_name, self.first_name, self.last_name))

U1 = User("xiaoming", "xiaohua")
U1.describe_user()
U1.greet_user()

# 复习点：
# 1、如果类里面有初始化函数  创建实例的时候 就必须要在实例里面传传递对应的参数
# 2、调用函数的时候 实例调用    class_01   实例函数、类函数、静态函数
