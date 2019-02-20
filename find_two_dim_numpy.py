#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2019/2/20 16:04
@author: Gaoqun Ma
@file: find_two_dim_numpy.py
"""
"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
class Solution:
    def Find(self, target, array):
        if not array:
            return False

        rows = len(array)
        cols = len(array[0])
        row, col = rows - 1, 0
        while row >= 0 and col <= cols - 1:
            if array[row][col] == target:
                return True
            elif array[row][col] < target:
                col = col + 1
            else:
                row = row - 1
        return False

"""
知识点：
1.明确数据的索引的时间复杂度为1
2.数组只有len的方法，numpy才有shape，size和len的方法，所以想知道数组的维度只能len
3.一个数组若为空，直接判断即可，为空输出为false
方法一：
直接遍历二维数组，时间复杂度为（N*M）
方法二：
从左下角或者右上角一步一步的搜索，举例来说，从左下角开始，如果target大于本值，向左移动；若小于本值，则向上移动。这也是不从左上角开始的原因
如果大于，左上角可以有两个移动方向，移动的方向就是不确定的了
"""

