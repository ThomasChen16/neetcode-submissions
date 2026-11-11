class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using pointers
        index1 = 0
        index2 = len(numbers) - 1

        # loop till index1 < index2
        while index1 < index2:
            # calculate sum
            sum = numbers[index1] + numbers[index2]

            if sum == target:
                return [index1+1, index2+1]
            # if sum is less than target increment index1
            elif sum < target:
                index1 += 1
            # if sum is greater than target decrement index2
            else:
                index2 -= 1
        
        return []

