class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        pal_str = ''
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1] and len(temp)>1:
                    if len(temp) > len(pal_str):
                        pal_str = temp
        if pal_str == '':
            return s[0]
        else:
            return pal_str

    def palDP(self, s):
        n = len(s)
        table = [[0 for x in range(n)] for x in range(n)]

        max_length = 1
        for i in range(n):
            table[i][i] = True

        start = 0

        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                start = i
                max_length = 2
        k = 3
        while k <= n:
            for i in range(0, n-k+1):
                j = i + k - 1
                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k
            k = k+1
        return s[start:start + max_length]



test = Solution()
test.palDP('abcdefaa')
