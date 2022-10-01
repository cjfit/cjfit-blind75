# Solution 1. Not ideal implementation
# Time: o(n)
# Memory: o(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            rem = target-nums[i]
            # check if in list and indices don't match
            if rem in nums and nums.index(rem) != i:
                return [i, nums.index(rem)]

# Solution 2. Another very inefficient naive implementation
# Time: o(n^2)
# Memory: o(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

# Solution 3. Efficient HashMap implementation
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