# Leetcode-2
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers
# and return it as a linked list.




class Node:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    #Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    #Add the contents of the two list and return the head
    #Node of resultant list
    def addtwonumber(self, l1, l2):
        prev = None
        carry = 0
        temp = None

        while l1 is not None or l2 is not None:
            fdata = 0 if l1 is None else l1.val
            sdata = 0 if l2 is None else l2.val
            lsum = carry + fdata + sdata

            #Update the carry
            carry = 1 if lsum >= 10 else 0

            #Update the sum
            lsum = lsum % 10 if lsum >= 10 else lsum

            #Create a new node with temp
            temp = Node(lsum)

            # if this is a new node set it to head of the resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            #Set prev for next insertions
            prev = temp

            # Shift the data to the next nodes
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            temp.next = Node(carry)

    def printList(self):
        temp = self.head
        res_list = []
        while temp is not None:
            res_list.append(temp.val)
            temp = temp.next
        print(res_list)

first = Solution()
second = Solution()

# Pushing the first linked lists
first.push(1)
first.push(8)

# Pushing the second linked lists
second.push(0)

res = Solution()
res.addtwonumber(first.head, second.head)

res.printList()

