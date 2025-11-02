class Patient:
    def __init__(self, name, urgency):
        if not isinstance(name, str) or not name:
            raise ValueError("Patient name cannot be empty.")
            
        if not (1 <= urgency <= 10):
            raise ValueError("Urgency level must be an integer between 1 (most urgent) and 10.")
            
        self.name = name
        self.urgency = urgency
        
    def __repr__(self):
        return f"Patient(name='{self.name}', urgency={self.urgency})"

    def __lt__(self, other):
        return self.urgency < other.urgency

# --- Example Usage ---

if __name__ == "__main__":
    
    print("--- Patient Class Test ---")
    
    p1 = Patient("Alice", 1)  # Top Priority
    p2 = Patient("Bob", 5)    # Medium Priority
    p3 = Patient("Charlie", 10) # Low Priority

    print(f"Patient 1: {p1}")
    print(f"Patient 2: {p2}")
    
    print(f"\nIs P1 more urgent than P2? (p1 < p2): {p1 < p2}")
    print(f"Is P2 more urgent than P3? (p2 < p3): {p2 < p3}")
    
    print("\n--- Error Handling Test ---")
    try:
        p_fail = Patient("Doris", 11)
    except ValueError as e:
        print(f"Caught expected error (11): {e}")

    try:
        p_fail = Patient("Doris", 0)
    except ValueError as e:
        print(f"Caught expected error (0): {e}")


class MinHeap:
    def __init__(self):
        self.data = []
        
    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]
        
    def _get_parent_index(self, index):
        if index == 0:
            return None 
        return (index - 1) // 2

    def _get_left_child_index(self, index):
        left_index = 2 * index + 1
        if left_index < len(self.data):
            return left_index
        return None

    def _get_right_child_index(self, index):
        right_index = 2 * index + 2
        if right_index < len(self.data):
            return right_index
        return None



# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    
    # Initialize a queue and manually add dummy data for testing index helpers
    queue = MinHeap()
    # P1 (index 0) is the root
    queue.data = [Patient("P1", 1), Patient("P2", 2), Patient("P3", 3), Patient("P4", 4), Patient("P5", 5)]
    print(f"Test data indices: [0:P1, 1:P2, 2:P3, 3:P4, 4:P5]")

    print("\n--- Testing Index Helpers ---")
    
    # Test index 1 (P2)
    p2_index = 1
    print(f"P2 (Index {p2_index}):")
    print(f"  Parent index: {queue._get_parent_index(p2_index)} (Should be 0 - P1)")
    print(f"  Left child index: {queue._get_left_child_index(p2_index)} (Should be 3 - P4)")
    print(f"  Right child index: {queue._get_right_child_index(p2_index)} (Should be 4 - P5)")
    
    # Test index 0 (Root, P1)
    p1_index = 0
    print(f"\nP1 (Index {p1_index}):")
    print(f"  Parent index: {queue._get_parent_index(p1_index)} (Should be None)")
    print(f"  Left child index: {queue._get_left_child_index(p1_index)} (Should be 1 - P2)")

    # Test index 4 (Leaf, P5)
    p5_index = 4
    print(f"\nP5 (Index {p5_index}):")
    print(f"  Left child index: {queue._get_left_child_index(p5_index)} (Should be None)")