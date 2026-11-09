import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for number in nums:
            # Add value to dict
            if number not in dict:
                dict[number] = 1
            else:
                # Increment dict
                dict[number] += 1
        
        # Return top k
        return heapq.nlargest(k, dict, key=dict.get)