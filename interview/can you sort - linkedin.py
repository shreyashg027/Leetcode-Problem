from collections import Counter
class Solution:
    def customMax(self, arr):
        dictchar = Counter(arr)
        # print(dictchar)
        print(dictchar.most_common())
        print(sorted(dictchar.items(), key=lambda pair: pair[1]))


test = Solution()
test.customMax([4,5,6,5,4,3])