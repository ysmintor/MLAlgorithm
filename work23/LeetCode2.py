# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_l1 = l1
        cur_l2 = l2
        carry = 0
        head = ListNode(None)
        cur_node = head
        while (cur_l1 is not None) and (cur_l2 is not None):
            s = cur_l1.val + cur_l2.val + carry
            cur_node.next = ListNode(s % 10)
            carry = s // 10

            cur_node = cur_node.next
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next

        if cur_l1 is None:
            cur_l1 = cur_l2

        while cur_l1 is not None:
            s = cur_l1.val + carry
            cur_node.next = ListNode(s % 10)
            carry = s // 10

            cur_node = cur_node.next
            cur_l1 = cur_l1.next

        if carry == 1:
            cur_node.next = ListNode(1)
        a = str("aa").split()
        return head.next