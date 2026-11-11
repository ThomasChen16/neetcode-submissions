class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove spaces and special characters from s and make undercase
        result_s = "".join(char for char in s if char.isalnum()).lower()
        print("result", result_s)

        # pointers for beginning and end of s
        left = 0
        right = len(result_s) - 1

        # loop while left is less than right
        while left < right:
            # if different characters return false
            if result_s[left] != result_s[right]:
                return False
            # increment/decrement if same
            left += 1
            right -= 1
        
        return True
        
