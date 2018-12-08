class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = bin(int(a,2)+int(b,2))
        return sum[2:]


test = Solution()
ans = test.addBinary("100",
                     "110010")
print(ans)


