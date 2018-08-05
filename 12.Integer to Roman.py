class Solution:
    def intToRoman(self, num):
        s = ''
        while num >=1000:
            s += 'M'
            num -= 1000
        while 900 <= num < 1000:
            s += 'CM'
            num -= 900
        while 500 <= num < 900:
            s += 'D'
            num -= 500
        while 400 <= num < 500:
            s += 'CD'
            num -= 400
        while num >= 100:
            s += 'C'
            num -= 100
        while 90 <= num < 100:
            s += 'XC'
            num -= 90
        while num >= 50:
            s += 'L'
            num -= 50
        while 40 <= num < 50:
            s += 'XL'
            num -= 40
        while num >= 10:
            s += 'X'
            num -= 10
        while num == 9:
            s += 'IX'
            num -= 9
        while 5 <= num < 9:
            s += 'V'
            num -= 5
        while num == 4:
            s += 'IV'
            num -= 4
        while 4 > num > 0:
            s += 'I'
            num -= 1
        return s







test = Solution()
ans = test.intToRoman(1994)
print(ans)
