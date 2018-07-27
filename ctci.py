class Solution:
    def checkPermutationOfPalindrome(self, str):
        charDict = dict()
        for char in str:
            if not char in charDict:
                charDict[char] = 1
            else:
                charDict[char] += 1
        # print(charDict)
        flag = 0
        for char in charDict:
            if charDict[char]%2 !=0:
                flag += 1
        if flag == 1:
            return True
        return False


test = Solution()

ans = test.checkPermutationOfPalindrome('aaaaa')
print(ans)
