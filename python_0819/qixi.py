#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/8/26 23:33  
# @File   ：qixi.py

'''
import string
l = string.ascii_letters
s = []
s.append(l[34])
s.append(l[11])
s.append(l[14])
s.append(l[21])
s.append(l[4])
s.append(l[24])
s.append(l[14])
s.append(l[20])
s.insert(1, " ")
s.insert(6, " ")
string = "".join(s)
print(string)
'''
'''
print(chr(73))
print(chr(76))
print(chr(79))
print(chr(86))
print(chr(86))
print(chr(69))
print(chr(85))
'''

print("\n".join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
