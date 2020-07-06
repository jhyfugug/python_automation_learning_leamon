#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author ： 'jhyfugug'
# @Time   ： 2020/6/15 1:37
# @File   ：class_str.py
# 字符串的一些使用
s = 'hello!'

# 1：字符串里面元素：单个字母、数字、汉字、单个符号 都称为一个元素
# len（数据） 统计数据的长度 print（len（数据））
print(len(s))
# 2：字符串取值：字符串名[索引值]
# 索引：正序是从0开始标记，反序是从-1开始取
print(s[5])
print(s[-1])
# 字符串多个取值：切片   字符串名[索引头：索引尾：步长] 步长默认为1
print(s[1:5:1])  # 1 2 3 4  # 取头不取尾
print(s[1:5:2])  # 1 3
print(s[:4])  # 0 1 2 3
print(s[3:])  # 4 5 6

# 小题目 ：请利用切片，倒序输出s的值，输出结果为 ！olleh
print(s[-1:-7:-1])  # -1 -2 -3 -4 -5 -6
print(s[::-1])

# 字符串的分割 字符串.split(可以指定切割元素，切割次数)
# 返回一个列表类型的数据   列表里面的子元素都是字符串类型
# 指定的切割符被切割走了

print(s.split())

# 字符串的替换 字符串.replace（指定替换值，新值，替换次数）
new = s.replace('o', '@')
print(new)
print(s)
#
# 字符串的去除指定字符   字符串.strip(指定字符)
# 1：默认去掉空格   #2:只能去掉头和尾指定的字符
s = ' hello!'
print(len(s))
new = s.strip('!')
print(len(new))
print(new)

# 字符串的拼接 +  要保证左右两边的变量值的类型一致（要么加引号，要么强制类型转换）
s_1 = 'python12'
s_2 = '武汉加油'
s_3 = 666
print(s_1 + s_2)
print(s_1 + s_2 + str(s_3))

# 字符串的格式化输出    % format
age = 18
name = "木头人"
score = 99.99
print("name" + name + "今年" + str(age) + "岁！")  # 无法判断age的类型，需要强制转换很麻烦

# 格式化输出1： format  特点 {}   用{}来占位置
print("{}今年{}岁！".format(name, age))
# 格式化输出2： %  %s字符串 %d整型 %f浮点型
print("%s今年%d岁！考了%f分" % (name, age, score))


