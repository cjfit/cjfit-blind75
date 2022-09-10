# Solution 1. (Least Optimal)
# Time: o(n^2)
# Memory: o(n^2)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
    
        for(a, b) in zip(nums, nums[1:]):
            if a == b:
                return True
        return False

# Solution 2.
# Time: o(n^2)
# Memory: o(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        for i in range(0, len(nums)):
            if nums[i] in nums[:i]:
                return True
                
        return False

# Solution 3. HashMap (Most Optimal)
# Time: o(n)
# Memory o(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
            
        return False