import re


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = pow(2, 31)-1
        MIN_INT = pow(-2, 31)
        reObj = re.match(r' *[-,+]?[0-9]+', str)
        if reObj:
            num = int(reObj.group().strip(' '))
            if num > MAX_INT:
                return MAX_INT
            elif num < MIN_INT:
                return MIN_INT
            else:
                return num
        else:
            return 0


test = Solution()
ans = test.myAtoi('+1')
print(ans)
