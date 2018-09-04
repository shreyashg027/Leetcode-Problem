# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = ListNode(0)
        l3 = l3.next
        printList = []
        while l1 is not None and l2 is not None:
            l3 = ListNode(l1.val+l2.val+carry)
            carry = 0
            if l3.val > 9:
                l3.val %= 10
                carry = 1
            printList.append(l3.val)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            l3 = ListNode(l1.val+carry)
            carry = 0
            if l3.val > 9:
                l3.val %= 10
                carry = 1
            printList.append(l3.val)
            l3 = l3.next
            l1 = l1.next

        while l2 is not None:
            l3 = ListNode(l2.val+carry)
            carry = 0
            if l3.val > 9:
                l3.val %= 10
                carry = 1
            printList.append(l3.val)
            l3 = l3.next
            l2 = l2.next
        if carry>0:
            printList.append(carry)
        return printList


            