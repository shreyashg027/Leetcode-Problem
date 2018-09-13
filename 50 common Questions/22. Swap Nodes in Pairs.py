class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node and node.next:
            node.next.val,node.val = node.val, node.next.val
            node = node.next.next
        return head
