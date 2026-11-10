class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode it with length by each element and # separating the element
        encoded_string = ""

        for element in strs:
            encoded_string += str(len(element)) + "#" + element

        return encoded_string

    def decode(self, s: str) -> List[str]:
        # decode it with identify the length of each element and then the string itself after #
        decoded_strs = []
        i = 0

        # Loop through s
        while i < len(s):
            j = i

            # Find the separator #
            # Loop till we find #
            while s[j] != "#":
                j += 1
            
            # Extract and convert to integer length
            length = int(s[i:j])

            # Extract the actual string based on length
            # Start from the location after #
            start = j + 1
            word = s[start : start + length]

            # Append word
            decoded_strs.append(word)

            # Update i to move to next string
            i = start + length

        return decoded_strs


