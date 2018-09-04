# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = l3 = ListNode(0)
        printList = []
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                printList.append(l1.val)
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                printList.append(l2.val)
                l2 = l2.next
                l3 = l3.next
        while l1 is not None:
            printList.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            printList.append(l2.val)
            l2 = l2.next
        return printList


test = Solution()
list1 = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(3)
list2 = ListNode(1)
f2 = ListNode(3)
f3 = ListNode(4)

list1.next = e2
e2.next = e3

list2.next = f2
f2.next = f3

ans = test.mergeTwoLists(list1, list2)
print(ans)

