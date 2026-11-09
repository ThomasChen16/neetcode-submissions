class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for index, number in enumerate(nums):
            # Difference between target and number
            diff = target - number
            # If inside dict return the index
            if number in dict:
                return [dict[number], index]
            
            # Add the diff and its index to dict
            dict[diff] = index
        
        return []
