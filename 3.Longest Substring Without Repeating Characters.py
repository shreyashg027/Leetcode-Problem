# Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.
NO_OF_CHARS = 256
class Solution:
    def lengthOfLongestSubstring(self, s):
        cur_len = 1
        max_len = 1
        n = len(s)


        visited = [-1]*NO_OF_CHARS

        visited[ord(s[0])] = 0

        for i in range(1, n):
            index = visited[ord(s[i])]
            # print('cur', cur_len)
            if index == -1 or i - cur_len > index:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = i - index
            visited[ord(s[i])] = i
        if cur_len > max_len:
            max_len = cur_len
        return max_len


test = Solution()
ans = test.lengthOfLongestSubstring('abbbbc')
print(ans)



