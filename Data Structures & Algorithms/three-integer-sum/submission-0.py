class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Using pointers
        index1 = 0
        index2 = len(nums) - 1

        # Sort the list
        nums.sort()

        # Holds triplet results
        results = []

        # Loop through list
        for index, value in enumerate(nums):
            # Handle duplicates in value
            if index > 0 and value == nums[index - 1]:
                continue

            # Pointer inside loop as each time the previous
            index1 = index + 1    # index + 1 as we do not need to check previous values as it was considered in the nested loop
            index2 = len(nums) - 1
            

            while index1 < index2:
                # Total
                sum = value + nums[index1] + nums[index2]

                # Triplet found
                if sum == 0:
                    results.append([value, nums[index1], nums[index2]])

                    # Increment first to start while loop
                    index1 += 1

                    # Loop index1 till no duplicate value
                    while index1 < index2 and nums[index1] == nums[index1-1]:
                        index1 += 1

                elif sum < 0:
                    index1 += 1
                else:
                    index2 -= 1
        
        return results


