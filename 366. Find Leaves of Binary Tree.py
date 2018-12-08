# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findLeaves(self, root, lst, prev):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            if root.left is None and root.right is None:
                print('prev-', prev.val)
                print('current-', root.val)
                lst.append(root.val)
                #prev.left = None
                #prev.right = None
            else:
                prev = root
                self.findLeaves(root.left, lst, prev)
                self.findLeaves(root.right, lst, prev)

        return lst


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left, t1.right = t2, t3
t2.left, t2.right = t4, t5

test = Solution()
lst = []
ans = test.findLeaves(t1, lst, None)
print(ans)
