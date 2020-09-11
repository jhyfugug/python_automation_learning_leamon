#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/9/9 20:50  
# @File   ：class_01.py

# 超继承

class MathMethod:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("I am parent method", self.a + self.b)

    def sub(self):
        print(self.a - self.b)


class MathMethod_1(MathMethod):
    def divide(self):  # 拓展
        return self.a / self.b

    def add(self):  # 重写
        super(MathMethod_1, self).add()  # 子类调用父类相同的方法
        print("I am son menthod", self.a + self.b + 10)


MathMethod_1(5, 6).add()
