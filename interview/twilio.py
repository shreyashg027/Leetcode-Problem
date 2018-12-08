class Solution:
    def missingWords(self, s,t):
        ans = []
        a = s.split(' ')
        b = t.split(' ')
        j = 0
        for i in range(len(a)):
            if j == len(b):
                ans.append(a[i])
            elif a[i] != b[j]:
                ans.append(a[i])
            else:
                j += 1
        return ans


test = Solution()
ans = test.missingWords(
    'I love programming',
    'programming'
)

print(ans)