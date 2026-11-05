class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        integer_count = {}

        for i in nums:
            if i not in integer_count:
                integer_count[i] = 1
            else:
                return True
        
        return False