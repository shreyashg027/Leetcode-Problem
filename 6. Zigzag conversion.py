class Solution:
    def convert(self, s, numRows):
        if len(s) == 1 or numRows >= len(s) or numRows==1:
            return s
        L = ['']*numRows
        i, step = 0, 1
        for char in s:
            L[i] += char
            if i == 0:
                step = 1
            if i == numRows-1:
                step = -1
            i += step
        return ''.join(L)


test = Solution()
ans = test.convert('abc', 1)
print(ans)
