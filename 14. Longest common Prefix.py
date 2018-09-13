class Solution:
    def longestCommonPrefix(self, strs):
        new_str = ""
        strs = sorted(strs)
        if not strs:
            return ""
        if len(strs[0]) == 0:
            return ""
        first_string = strs[0]
        for j in range(len(first_string)):
            k = 0
            for i in range(1, len(strs)):
                if first_string[j] != strs[i][j]:
                    return "" if j == 0 else new_str
                else:
                    k += 1
                if k == len(strs)-1:
                    new_str += first_string[j]
                    # print(first_string[j])
        return new_str


test = Solution()
ans = test.longestCommonPrefix(["a"])
print(ans)
