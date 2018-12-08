class Solution:
    def removechar(self, str):
        l = []
        op = ['+', '-', '*', '/']
        new_s = ''
        flag = 0
        for i in str:
            # if i in op:
            if i.isdigit() or i == '.' or (i== '-' and not flag) :
                new_s += i
                flag = 1
                # print(i)
            elif i in op:
                l.append(new_s)
                l.append(i)
                new_s = ''
                flag = 0
        l.append(new_s)
        # print(l)
        l.reverse()
        print(l)
        str = ''.join(l)
        return str

test = Solution()
ans = test.removechar('-993-7777')
print(ans)