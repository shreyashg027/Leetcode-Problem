class Solution:
    def isPalindrome(self, x):
        origin = x
        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev*10 + digit
            x = int(x/10)
        if origin == rev:
            return bool(1)
        else:
            return bool(0)



test = Solution()
ans = test.isPalindrome(+121)
print(ans)