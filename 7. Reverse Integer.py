import sys
class Solution:
    def reverse(self, x):
        print(sys.getsizeof(x))
        if x > 2147483647 or x < -2147483647:
            return 0
        rev = 0
        flag = 0
        if x < 0:
            x = -x
            flag = 1
        while x > 0:
            digit = x % 10
            rev = rev*10 + digit
            # print('rev', rev)
            x = int(x / 10)
            # print('x', x)
        if flag:
            return -rev
        else:
            return rev


test = Solution()
ans = test.reverse(-2147483648)
print(ans)
