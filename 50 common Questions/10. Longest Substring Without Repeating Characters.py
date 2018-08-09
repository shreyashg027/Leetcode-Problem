class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        if s ==" ":
            return 1
        cur_len = 0
        max_len = 0
        dictChar = {}
        i = 0
        while i < len(s):
            if s[i] not in dictChar:
                dictChar[s[i]] = i
                cur_len += 1
                if i == len(s)-1 and cur_len>max_len:
                    max_len = cur_len
            else:
                if cur_len > max_len:
                    max_len = cur_len
                i = dictChar.get(s[i])+1
                dictChar = {}
                dictChar[s[i]] = i
                cur_len = 1
            i+=1
        return max_len


test = Solution()
ans = test.lengthOfLongestSubstring("abcb")
print(ans)

