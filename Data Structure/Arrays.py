class Solution:
    def rotLeft(self, a, d):
        n = len(a)
        rotatedArr = [0]*n
        for i in range(n):
            rotNum = d % n
            rotatedArr[i] = a[rotNum]
            d = d+1
        return rotatedArr

    # New Year Chaos
    def minimumBribes(self, q):
        n = len(q)
        count = 0
        for i, v in enumerate(q):
            if v-1-i > 2:
                return 'Too chaotic'
        for i in range(n):
            for j in range(i, n-1):
                if q[j] > q[j + 1]:
                    q[j], q[j + 1] = q[j + 1], q[j]
                    count += 1
        return count



test = Solution()
test.rotLeft([1, 2, 3, 4, 5], 4)
ans = test.minimumBribes()
print(ans)