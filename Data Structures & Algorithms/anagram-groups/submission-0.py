class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary
        dict = {}
        if len(strs) == 0:
            return [[""]]

        
        # the key for the character could be the sorted version
        for char in strs:
            # sort the char and turn it back to a string
            sorted_char = "".join(sorted(char))
            if sorted_char in dict:
                dict[sorted_char].append(char)
            else:
                # new entry
                dict[sorted_char] = [char]
        
        return list(dict.values())