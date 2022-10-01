// Solution 1. Optimized Runtime

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> counts = new HashMap<Integer, Integer>();
        
        for (int i=0; i< nums.length; i++){
            int rem = target-nums[i];
            
            if (counts.containsKey(rem)) {
                return new int[] {counts.get(rem), i};
            }
            counts.put(nums[i], i);
        }
        
        return new int[] {};
    }
    
}
