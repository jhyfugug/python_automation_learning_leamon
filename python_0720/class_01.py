#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/7/20 23:18  
# @File   ：class_01.py

# relative path   or   absolute path

# 疑问： if we will open operator a file,whether use relative path or absolute path?

import os
# create a make directory/create a folder
# os.mkdir("Alisa")

# cross-level new folder    use / symbol
# os.mkdir("Alisa")
# os.mkdir("Alisa/vict")  # relative path   must upper layer path exist

# os.mkdir("D:\\test_python13")    # absolute path
# os.mkdir(r"D:\test_python13")    # escape symbol

# delete   delete file need one by one to go
# os.rmdir(r"D:\test_python13")
# os.remove(r"D:\test_python13")

'''
# get path  workspace    到最后一级
path_1 = os.getcwd()
print("this path is {0}".format(path_1))

# 绝对路径   获取到绝对路径    具体到模块名
path_2 = os.path.realpath(__file__)
print("this path is {0}".format(path_2))

# 拼接路径
new_path_1 = os.getcwd()
'''

# 拓展题
# 给出一个路径，请打印出所有的路径（直到这个路径下没有目录为止）
for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
        os.listdir(os.path.join(os.getcwd(), path))
        print("{0}还需要进一步处理".format(path))
    else:
        print("This is a final path：", os.path.join(os.getcwd(), path))




