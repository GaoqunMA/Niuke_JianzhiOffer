#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2019/2/21 15:22
@author: Gaoqun Ma
@file: reConstructBinaryTree.py
"""
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含
重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树
并返回。
"""
class TreeNode:
    def __init(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        index = tin.index(pre[0])
        left = tin[0:index]
        right = tin[index+1:]
        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:len(left)+1], left)
        root.right = self.reConstructBinaryTree(pre[len(left)+1:], right)
        return root

"""
知识点：
1.list的索引方法为index，返回的是索引值的位置；str的索引方法为find,返回的为第一次出现该索引字符的位置
2.递归，树天然就是递归，以后碰到树的问题，首先想到的解决方法应该为递归。
递归的核心思想有两个：
递归停止问题：即0,1时刻验证方法是否准确
泛化问题：由n如何推广到n+1
总体来说，递归就是将一个问题不断的去缩小，不断的缩小，最后得以解决。
"""