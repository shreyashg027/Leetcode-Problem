# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre =  ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val ==head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                head = head.next
                pre = pre.next
        return dummy.next


l = ListNode(1)
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(3)
l.next = l1
l1.next = l2
l2.next = l3
l3.next = l4


test = Solution()
test.deleteDuplicates(l)