class Solution:
    def runnerScore(self, arr):
        arr = sorted(arr, reverse=True)
        for i in range(len(arr)-1):
            if arr[i]!= arr[i+1]:
                print(arr[i+1])
                break


test = Solution()
# ans = test.runnerScore([2, 3, 6, 6, 5])
# print(ans)

m1,m2 = float('inf'),float('inf')
lis = [20,20,19,19,21]
for score in lis:
    if score <= m1:
        m1,m2 = score,m1
    elif score < m2:
        m2 = score

print(m1, m2)