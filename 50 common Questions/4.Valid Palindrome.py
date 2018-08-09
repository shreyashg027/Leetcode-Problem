class Solution:
    def isPalindrome(self, s):
        if s == '':
            return True
        s = ''.join([i for i in s if i.isalnum()])
        s = s.lower()
        if s == s[::-1]:
            return True
        return False



test = Solution()
ans = test.isPalindrome("0P")
print(ans)
