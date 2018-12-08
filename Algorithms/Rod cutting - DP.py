class Solution:
    def rodCutting(self, l, arr):
        t = [[0 for j in range(0,l+1)] for j in range(1, len(arr))]
        for i in range(1, len(arr)-1):
            for j in range(0,l+1):
                if j >= i:
                    t[i][j] = max(t[i-1][j], t[i][j-i]+arr[i])
                else:
                    t[i][j] = t[i-1][j]
        return t[i][j]


test = Solution()
ans = test.rodCutting(5, [0, 2, 5, 7, 8])
print(ans)