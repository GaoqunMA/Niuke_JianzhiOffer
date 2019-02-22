#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2019/2/21 16:47
@author: Gaoqun Ma
@file: Fibonacci.py
"""
"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n-2) + self.Fibonacci(n-1)

def fib(n):
    if n <= 1:
        return n
    fib_list = [0,1]
    num = 1
    while n > 0:
        fib_list[0], fib_list[1] = fib_list[1], fib_list[0] + fib_list[1]
        n-=1
    return fib_list[0]

"""
知识点：

方法一：递归，找到特殊的点，然后由n泛化到n+1
方法二：斐波那契数列实际上只是需要它倒数两个数的位置，为最大减少空间复杂度，可以直接在这两个位置
不断复制
"""