class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Choose two lines that can hold the maximum amount of water

        best_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            # Calculate current area
            current_area = min(heights[left], heights[right]) * (right - left) 

            # Compare if new area is the largest
            if best_area < current_area:
                best_area = current_area

            # Determine which pointer to move
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
                right -= 1

        return best_area