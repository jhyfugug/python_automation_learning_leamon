#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/8/4 0:12  
# @File   ：class_02.py

# 异常处理
import os

try:
    os.mkdir("class_01.py")
except FileExistsError as e:
    print("Your worry is {0}".format(e))
    print("文件已存在！")
    file = open("error.txt", "a+", encoding="utf-8")
    file.write(str(e))
    file.close()
finally:    # 不管报不报错，我都会执行这条语句的
    print("Please come on！ keep energic！")
