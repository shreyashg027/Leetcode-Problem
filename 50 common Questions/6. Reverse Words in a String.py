class Solution(object):
    def reverseWords(self, s):
        arr = s.strip(' ').split()
        return ' '.join(x for x in arr[::-1])


test = Solution()
ans = test.reverseWords('the sky is blue')
print(ans)