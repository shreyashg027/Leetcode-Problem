import re


class Solution:
    def isNumber(self, s):
        s = s.strip()
        if not s:
            return False
        reObj = re.match(r"^[+-]?(\d+(\.\d*)?|\.\d+)(e[-+]?[0-9]+)?$", s)
        return True if reObj else False


test = Solution()
ans = test.isNumber('e9')
print(ans)

