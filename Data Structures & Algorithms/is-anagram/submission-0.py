class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If not the same length we already know it doesn't match
        if len(s) != len(t):
            return False

        character_dict = {}
        # Fill up character_dict with s first
        for char in s:
            if char not in character_dict:
                character_dict[char] = 1
            else:
                character_dict[char] += 1
        
        # Subtract charcter_dict with t after
        for char in t:
            # Different character
            if char not in character_dict:
                return False
            else:
                character_dict[char] -= 1
        
        # Check if any key in character_dict isn't 0
        for key in character_dict:
            if character_dict[key] != 0:
                return False
        
        return True