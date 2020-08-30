#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/8/24 23:45  
# @File   ：class_03.py

# 继承

class RobotOne:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def walking_on_ground(self):
        print(self.name+"可以平地行走")

    def robotInfo(self):
        print("{0}年生产的机器人{1}，是中国研发的".format(self.year, self.name))

'''
class RobotTwo:

    def __init__(self, year, name):
        self.year = year
        self.name = name

    def walking_on_ground(self):
        print(self.name + "可以平地行走")

    def walking_avoid_block(self):
        print(self.name+"can avoid block")

    def robotInfo(self):
        print("{0}年生产的机器人{1}，是中国研发的".format(self.year, self.name))

'''
# 继承    优化
# class RobotTwo(RobotOne):

class RobotTwo():

    def __init__(self, year, name):
        self.year = year
        self.name = name

    def walking_on_ground(self):
        print(self.name + "可以平地行走，平稳地行走")

    def walking_avoid_block(self):
        self.robotInfo()
        print(self.name+" can avoid block")

# r2 = RobotTwo("1990", "xiaowang")
# # r2.robotInfo()
# r2.walking_on_ground()

# 多继承
class RobotThree(RobotOne, RobotTwo):   # 多继承，就近原则

    def jump(self):
        print(self.name+"可以单膝跳跃")

r3 = RobotThree("1990", "dawang")
r3.walking_on_ground()
r3.walking_avoid_block()
r3.jump()
r3.robotInfo()

# 超继承
