class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dictChar  = {}
        for i,item in enumerate(B):
            if item not in dictChar:
                dictChar[item] = i
        P = [0 for i in range(len(A))]
        for i in range(len(A)):
            if A[i] in dictChar:
                P[i] = dictChar[A[i]]
        return P

test = Solution()
ans = test.anagramMappings('bat','tab')
print(ans)