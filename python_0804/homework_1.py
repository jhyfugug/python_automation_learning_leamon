#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/8/4 23:51  
# @File   ：homework_1.py

# 直角三角形
'''
for i in range(1, 6): # control row 1, 2, 3, 4, 5
    for j in range(1, i+1):
        print("* ", end="")
    print("")
'''

'''
# 等腰三角形

for i in range(1, 6):
    for j in range(1, 6-i):     # control per row begin blank
        print(" ", end="")
    for k in range(1, i+1):
        print("* ", end="")
    print("")

'''
'''
# optimize

def print_triangle(m):
    for i in range(1, m):
        for j in range(1, m-i):
            print(" ", end="")
        for k in range(1, i+1):
            print("* ", end="")
        print("")

if __name__ == '__main__':
    print_triangle(6)

'''
'''
# Multiplication Table   (九九乘法表)

for i in range(1, 10):
    for j in range(1, i+1):
        print("{0}*{1}={2} ".format(j, i, i*j), end="")
    print("")

'''

# 冒泡排序  利用for循环，完成a = [1, 7, 4, 89, 3, 4]

a = [1, 7, 4, 89, 3, 4]

for i in range(0, len(a)-1):
    for j in range(0, len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)


