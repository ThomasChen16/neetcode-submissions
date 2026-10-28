# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # If pairs is empty:
        if not pairs:
            return []
            
        # Copy that display each step of the insertion sort for pairs
        insertion_sort_array = [pairs.copy()]

        # start from the second element index 1
        for i in range(1, len(pairs)):
            # The element we want to position
            key = pairs[i]
            # Index of the last element in the sorted section
            j = i - 1

            # Move elements of pair that are greater than key to one position ahead of their current position
            # > only shifts when greater to help maintain relative order for same integer keys
            while j >= 0 and pairs[j].key > key.key:
                # Swap position of key and compored element
                pairs[j + 1] = pairs[j]
                # Update j
                j -= 1
            
            # If key is instead greater than pairs[j].key
            # Move key behind pairs[j].key
            pairs[j+1] = key

            # Update insertion_sort_array
            insertion_sort_array.append(pairs.copy())
        
        return insertion_sort_array
            
            
        