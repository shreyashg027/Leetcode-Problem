class Solution:
    def romanToInt(self, s):
        num = 0
        i = 0
        s += 'Z'
        while i<len(s):
            if s[i] == 'C' and s[i+1] == 'M':
                num += 900
                i += 1
            elif s[i] == 'C' and s[i+1] == 'D':
                num += 400
                i += 1
            elif s[i] == 'X' and s[i+1] == 'C':
                num += 90
                i += 1
            elif s[i] == 'X' and s[i+1] == 'L':
                num += 40
                i += 1
            elif s[i] == 'I' and s[i+1] == 'X':
                num += 9
                i += 1
            elif s[i] == 'I' and s[i+1] == 'V':
                num += 4
                i += 1
            elif s[i] == 'M':
                num += 1000
            elif s[i] == 'D':
                num += 500
            elif s[i] == 'C':
                num += 100
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'X':
                num += 10
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'I':
                num += 1
            i += 1
        return num


test = Solution()
ans = test.romanToInt('MCMXCIV')
print(ans)

