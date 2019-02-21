#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2019/2/20 16:59
@author: Gaoqun Ma
@file: replaceSpace.py
"""
"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
class Solution():
    def replaceSpace(self, s):
        if not s:
            return s
        else:
            replace_s = []
            s = list(s)
            for alpha in s:
                if alpha == ' ':
                    replace_s.append('%20')
                else:
                    replace_s.append(alpha)
            return ''.join(replace_s)

if __name__ == '__main__':
    gaoqun = Solution()
    s = gaoqun.replaceSpace('Ma Gao Qun')
    print s

"""
知识点：
1.str可以直接通过list()转化为list，也可以通过.split('')分割字符串变成数组
2.''.join(list)，可以将list中所有的字符串以指定形式拼接(非常重要，对于字符串去除数字等等有很好的应用)
3.字符串内置函数replace,' a b'.replace(' ', '20%')
方法一：
将字符串先转化为数组，然后做一个判断，在将数组中的字符拼接为字符串。
时间复杂度为(N)N为字符串的长度，空间复杂度为（N）
方法二：
使用正则表达式 import re 正则表达式只能用于字符串序列
https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000
此链接为正则表达式的详细介绍
基本公式：
\d 表示数字
\w 表示字母
\s 表示空格，制表等字符
. 任意字符
* 0个或任意个
+ 1个或任意个
？ 0个或1个
| 或的意思
正则表达式表达python的合法变量：[a-zA-Z\_][0-9a-zA-Z\_]*  由字母和下划线开头，后接任意数量数字
字母下划线的变量。
"""