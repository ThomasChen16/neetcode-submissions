class DynamicArray:
    
    def __init__(self, capacity: int):
        # Assign arguments to instance attribute
        self.capacity = capacity
        self.size = 0
        # Create array with capacity
        self.array = [0] * capacity        

    def get(self, i: int) -> int:
        # Return element at index i
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        # Set element at index i to n
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # Push element n to end of array
        # Check if array is already full if so resize it
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Pop and return the element at the end of the array
        # Update size
        self.size -= 1

        last_element = self.array[self.size]
        
        # Update array
        self.array[self.size] = 0

        return last_element

    def resize(self) -> None:
        # Double the capacity of the array
        self.capacity *= 2
        # Update array with new capacity with copying over old elements
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array


    def getSize(self) -> int:
        # Return number of elements in the array
        return self.size
    
    def getCapacity(self) -> int:
        # Return capacity of the array
        return self.capacity
