class Solution:
    def bubble_sort(self, q):
        n = len(q)
        for i in range(n):
            for j in range(i, n-1):
                if q[j] > q[j + 1]:
                    q[j], q[j + 1] = q[j + 1], q[j]
        return q

test = Solution()
ans = test.bubble_sort([2, 1, 5, 3, 4])
print(ans)
