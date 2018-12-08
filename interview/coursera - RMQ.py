class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.min = 9999
        self.left = None
        self.right = None

class segmentTree(object):
    def __init__(self, list):
        def create(list, left, right):
            if left > right:
                return None
            if left == right:
                node = Node(left, right)
                node.min = list[left]
                return node

            mid = (left + right) // 2

            root = Node(left, right)
            root.left = create(list, left, mid)
            root.right = create(list, mid+1, right)

            root.min = min(root.left.min,root.right.min)

            return root

        self.root = create(list, 0, len(list)-1)


    def minRange(self, i, j):
        def rangeMin(root, i, j):

            if root.start == i and root.end == j:
                return root.min

            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeMin(root.left, i, j)

            elif i >= mid + 1:
                return rangeMin(root.right, i, j)

            else:
                return min(rangeMin(root.left, i, mid) , rangeMin(root.right, mid+1, j))

        return rangeMin(self.root, i, j)

list_len,query_len = input().split(' ')
list = input().split(' ')
list = [int(x) for x in list]
arr = segmentTree(list)
for i in range(int(query_len)):
    q_1,q_2 = input().split(' ')
    print(arr.minRange(int(q_1),int(q_2)))


def Magical_binary_String(binString):
    list  = []

    st = ""
    for i,j in enumerate(binString):
        one_count = 0
        zero_count = 0
        st = ""
        greater = False
        for k,l in enumerate(binString[i:]):
            if l == '1':
                one_count = one_count + 1

            else:
                zero_count = zero_count +1

            st+=l
            print(one_count)

            if one_count == zero_count and greater:
                list.append(st)
            if one_count > zero_count:
                greater = True
            else:
                greater = False
    print(list)
    sort_list = sorted(list)
    return sort_list[-1]

