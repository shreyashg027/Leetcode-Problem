# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        prev = head
        cur = head.next
        while cur is not None and prev is not None:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        while head is not None:
            print(head.val)
            head = head.next
        # return head

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
ans = test.deleteDuplicates(l)
# print(ans)