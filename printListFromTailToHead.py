#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2019/2/21 14:53
@author: Gaoqun Ma
@file: printListFromTailToHead.py
"""
"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):

        if not listNode:
            return []
        else:
            val_list_head_to_tail = []
            p = listNode
            while p:
                val_list_head_to_tail.append(p.val)
                p = p.next
            val_list_tail_to_head = []
            while val_list_head_to_tail:
                val_list_tail_to_head.append(val_list_head_to_tail.pop())
            return val_list_tail_to_head

    def getPrint(self, listNode):
        if not listNode:
            return
        self.getPrint(listNode.next)
        print listNode.val
"""
知识点：
1.python中的栈是通过list来实现的，list中的pop就是栈中的出栈。但是，python中的队列不是用list实现，因为
list来实现移动的时间复杂度为(N)
2.从尾到头明显反应的就是一个后进先出的结构，所以用栈比较妥当
方法二：可以使用递归，列表遍历用的最多的也是递归
"""