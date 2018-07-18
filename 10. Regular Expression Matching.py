class Solution:
    # def isMatch(self, s, p):
    def match(self, text, pattern):
        if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern)>= 2 and pattern[1] == '*':
            return self.match(text, pattern[2:]) or first_match and self.match(text[1:], pattern)
        else:
            return first_match and self.match(text[1:], pattern[1:])


test = Solution()
ans = test.match('aaaaaa', 'a*')
print(ans)
