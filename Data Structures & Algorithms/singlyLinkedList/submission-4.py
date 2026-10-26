class Node:
    def __init__(self, val):
        # Initialize attributes for Node
        self.value = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        # Initialize the head
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        current_index = 0

        # Traverse the list until we find the index or go out of bound
        while current is not None:
            if current_index == index:
                return current.value
            
            # Move current to the next node
            current = current.next
            # Increment index
            current_index += 1
        
        # if reach out of bounds
        return -1

    def insertHead(self, val: int) -> None:
        # Insert a node with val at the head of the list
        # Create new node
        new_node = Node(val)

        # Point that new node to the current head
        new_node.next = self.head

        # Update self.head to be the new node
        self.head = new_node

    def insertTail(self, val: int) -> None:
        # Insert a node with val at the tail of the list
        # Create new node
        new_node = Node(val)

        # If empty linked list
        if self.head is None:
            self.head = new_node
            return

        # Create temp node
        temp = self.head

        # Transverse temp pointer till it reach out of bound
        while temp.next:
            temp = temp.next
        
        # If reach out of bound set it pointer to the new node
        temp.next = new_node

    def remove(self, index: int) -> bool:
        # Remove the ith node
        # If linked list is empty
        if self.head is None:
            return False

        # If index is 0, remove the head
        if index == 0:
            self.head = self.head.next
            return True
        
        # Traverse to find the node before the index
        current = self.head
        count = 0

        while current is not None and count < index - 1:
            current = current.next
            count += 1
        
        # If current is still none after it reach out of bound means it doesn't exist
        if current is None or current.next is None:
            return False
        
        # Else target is found
        # Link the current pointer to next next node
        current.next = current.next.next

        return True

    def getValues(self) -> List[int]:
        # Return an array of all values in the linked list in order
        value_array = []

        # Transverse current till it goes out of bound
        current = self.head
        while current is not None:
            # append current node values to array
            value_array.append(current.value)
            current = current.next
        
        return value_array
        
    
            
