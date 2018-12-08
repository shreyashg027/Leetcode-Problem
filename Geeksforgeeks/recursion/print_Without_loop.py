class Solution:
    def printWithoutLoop(self,n,i):
        if n == i:
            print(n)
            return
        print(i)
        i+=1
        self.printWithoutLoop(n,i)


test = Solution()
ans = test.printWithoutLoop(10,1)
# print(ans)