#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/8/19 23:07  
# @File   ：class_01.py

# a = [1, 2, 3, 4]
# a.count()

class Teacher():
    name = "华华"
    age = "25"

    def cooking(self):  # 实例方法     self代表的是实例 t = Teacher（）
        print(self.name + "can cooking")

    @classmethod  # 类方法
    def swimming(cls):
        print("会做事")

    @staticmethod  # 静态方法
    def sing():
        print("I can sing")


# 类里面的三种方法
# ①实例方法
t = Teacher()
t.cooking()    # recommend this method

Teacher.cooking(t)

Teacher().cooking()

# ②类方法
Teacher.swimming()
t.swimming()

# ③静态方法
Teacher.sing()
t.sing()

# Summarize. 实例方法 self 、类方法 cls 、 静态方法 （普通方法） 的实例和雷鸣都可以直接调用
# differtia. 类方法 和静态方法 不可以调用类里面的属性值，需要什么参数，需要自己传值
# 什么时候使用静态方法和类方法呢？  当你的某个函数和其他类函数、类方法  没有关系的时候