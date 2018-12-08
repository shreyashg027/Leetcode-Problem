# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        beg = head
        l = 0
        while beg is not None:
            beg = beg.next
            l += 1
        x = l-n
        if x== 0:
            return head.next
        # print(x)
        prev = head
        cur = head.next
        flag = 0
        while cur is not None:
            if flag == x:
                prev.next = cur.next
            prev = prev.next
            cur = cur.next
            flag += 1
        while head is not None:
            print(head.val)
            head = head.next
        return prev


l = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(5)
l.next = l1
l1.next = l2
l2.next = l3
l3.next = l4


test = Solution()
test.removeNthFromEnd(l, 2)

