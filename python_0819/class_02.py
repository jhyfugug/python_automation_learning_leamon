#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/8/22 21:05  
# @File   ：class_02.py

# 初始化函数

class Teacher():
    def __init__(self, name):
        self.name = name
        self.age = 25

    def cooking(self):
        print("这是{0}的名字,且年龄为{1}".format(self.name, self.age))

    def coding(self, line, language="English"):
        print(self.name + "老师使用{0},敲了{1}行代码".format(language, line))

    def swimming(self, *args):
        for item in args:
            print(self.name+"会做{0}".format(item))


t1 = Teacher("华华")
# t1.cooking()
# t1.coding(10000)
t1.swimming("仰泳", "蛙泳", "蝶泳")
