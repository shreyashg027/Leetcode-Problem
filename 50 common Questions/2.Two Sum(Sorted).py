class Solution:
    def twoSum(self, numbers, target):
        if len(numbers) < 1:
            return False
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            l = i+1
            r = len(numbers)-1
            while l<=r:
                mid = int((l+r)/2)
                if compliment == numbers[mid]:
                    return [i+1, mid+1]
                elif compliment < numbers[mid]:
                    r = mid - 1
                elif compliment > numbers[mid]:
                    l = mid+1


test = Solution()
ans = test.twoSum([2, 7, 11, 15], 9)
print(ans)