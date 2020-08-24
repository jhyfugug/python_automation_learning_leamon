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

