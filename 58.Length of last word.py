class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        print(s)
        if s == '' or s == ' ':
            return 0
        lis = s.split()
        n = len(lis)

        return len(lis[n-1])


test = Solution()
ans = test.lengthOfLastWord('Hello World       ')
print(ans)