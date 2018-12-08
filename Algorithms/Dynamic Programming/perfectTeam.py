class Solution:
    def perfectteam(self, str):
        if not str:
            return 0
        dict = {}
        for char in str:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        print(dict)
        min = 9999
        for item, value in dict.items():
            if value < min:
                min = value
        return min





test = Solution()
ans = test.perfectteam('pcmpcmbbbzz')
print(ans)

a = 'Jdsad'
print(a.lower())