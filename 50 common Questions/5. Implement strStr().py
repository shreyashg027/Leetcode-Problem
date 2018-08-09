import re


class Solution:
    def strStr(self, haystack, needle):
        m = re.search(needle, haystack)
        if m:
            return m.start()
        return -1


test = Solution()
ans = test.strStr('hello', 'k')
print(ans)