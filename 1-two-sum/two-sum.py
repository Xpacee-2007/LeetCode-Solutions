class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}  # Stores the value and its index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already in our map
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, add the current number and its index to the map
            num_map[num] = i