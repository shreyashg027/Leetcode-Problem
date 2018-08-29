class Solution:
    def plusOne(self, digits):
        digits[len(digits)-1] += 1
        i = len(digits)-1
        while i > 0:
            print(i)
            if digits[i] > 9:
                digits[i] = 0
                digits[i-1] += 1
            i -= 1

        if digits[0]>9:
            digits[0] %= 10
            digits.insert(0, 1)

        return digits


test = Solution()
ans = test.plusOne([1,9,9,9])
print(ans)

