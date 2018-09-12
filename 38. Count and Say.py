class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        num = "11"
        finalStr = ""
        for i in range(3, n+1):
            # print(num)
            count = 1
            finalStr = ""
            for j in range(1, len(num)):
                if num[j-1] == num[j]:
                    count += 1

                else:
                    finalStr += str(count)
                    finalStr += num[j-1]
                    # print(finalStr)
                    count = 1
            finalStr += str(count)
            finalStr += num[j]
            num = finalStr

        return finalStr


test = Solution()
ans = test.countAndSay(30)
print(ans)

