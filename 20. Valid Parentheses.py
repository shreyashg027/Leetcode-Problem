class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if s == "":
            return True
        if len(s) == 1:
            return False
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == ')' and stack[len(stack)-2] == '(':
                stack.pop()
                stack.pop()
            elif s[i] == ']' and stack[len(stack)-2] == '[':
                stack.pop()
                stack.pop()
            elif s[i] == '}' and stack[len(stack)-2] == '{':
                stack.pop()
                stack.pop()
        return True if len(stack) == 0 else False


test = Solution()
ans = test.isValid("(])")
print(ans)