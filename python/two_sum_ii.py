# Solution 1. Inefficient HashMap implementation
# Same as TwoSum
# Time: o(n)
# Memory: o(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_occurences = {}
        for i, num in enumerate(nums):
            rem = target-num
            if rem in nums_occurences:
                return [nums_occurences[rem], i]
            nums_occurences[num] = i

# Solution 2. Similarly inefficient
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        
        while left != right:
            
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right-=1
            elif numbers[left] + numbers[right] < target:
                left+=1
            