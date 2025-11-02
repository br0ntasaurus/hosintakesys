class DoctorNode:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Doctor's name must be a non-empty string.")
            
        self.name = name
        self.left_report = None
        self.right_report = None
        
    def __repr__(self):
        return f"DoctorNode(name='{self.name}')"


class DoctorTree:
    
    
    def __init__(self, root_name=None):
        if root_name:
            self.root = DoctorNode(root_name)
        else:
            self.root = None

    def _search_node(self, current_node, target_name):
        if current_node is None: return None
        if current_node.name == target_name: return current_node
        found = self._search_node(current_node.left_report, target_name)
        if found: return found
        return self._search_node(current_node.right_report, target_name)

    def insert(self, parent_name, new_doctor_name, side):
        if self.root is None:
            raise RuntimeError(f"Cannot insert '{new_doctor_name}'. The tree is empty. Use set_root() first.")

        parent_node = self._search_node(self.root, parent_name)
        if parent_node is None:
            raise RuntimeError(f"Parent doctor '{parent_name}' not found in the tree.")

        new_node = DoctorNode(new_doctor_name)
        
        if side.lower() == 'left':
            if parent_node.left_report is not None:
                raise RuntimeError(f"The left report slot for '{parent_name}' is already taken.")
            parent_node.left_report = new_node
        elif side.lower() == 'right':
            if parent_node.right_report is not None:
                raise RuntimeError(f"The right report slot for '{parent_name}' is already taken.")
            parent_node.right_report = new_node
        else:
            raise ValueError(f"Invalid side '{side}'. Must be 'left' or 'right'.")
        



    def _preorder(self, node):
        """Root, Left, Right: Shows the hierarchy top-down."""
        result = []
        if node:
            result.append(node.name) 
            result.extend(self._preorder(node.left_report))
            result.extend(self._preorder(node.right_report))
        return result

    def _inorder(self, node):
        result = []
        if node:
            result.extend(self._inorder(node.left_report))
            result.append(node.name) 
            result.extend(self._inorder(node.right_report))
        return result

    def _postorder(self, node):
        result = []
        if node:
            result.extend(self._postorder(node.left_report))
            result.extend(self._postorder(node.right_report))
            result.append(node.name) 
        return result

    def traverse(self, traversal_type):
        if self.root is None:
            return []

        traversal_type = traversal_type.lower()
        if traversal_type == 'preorder':
            return self._preorder(self.root)
        elif traversal_type == 'inorder':
            return self._inorder(self.root)
        elif traversal_type == 'postorder':
            return self._postorder(self.root)
        else:
            raise ValueError("Invalid traversal type. Choose 'preorder', 'inorder', or 'postorder'.")


# --- Example Usage ---

if __name__ == "__main__":
    
    hospital_tree = DoctorTree("Dr. House (Chief)") 
    hospital_tree.insert("Dr. House (Chief)", "Dr. Wilson", "right")
    hospital_tree.insert("Dr. House (Chief)", "Dr. Cuddy", "left")
    hospital_tree.insert("Dr. Cuddy", "Dr. Chase", "left")
    hospital_tree.insert("Dr. Cuddy", "Dr. Cameron", "right")

    print("\n--- Traversal Results ---")
    
    pre_order_list = hospital_tree.traverse('preorder')
    print(f"Pre-Order (Root, L, R):   {pre_order_list}")
    
    in_order_list = hospital_tree.traverse('inorder')
    print(f"In-Order (L, Root, R):    {in_order_list}")
    
    post_order_list = hospital_tree.traverse('postorder')
    print(f"Post-Order (L, R, Root):  {post_order_list}")


class EmergencyQueue:

    def _get_parent_index(self, index):
        if index == 0: return None
        return (index - 1) // 2

    def _get_left_child_index(self, index):
        left_index = 2 * index + 1
        return left_index if left_index < len(self.data) else None

    def _get_right_child_index(self, index):
        right_index = 2 * index + 2
        return right_index if right_index < len(self.data) else None


    def _heapify_up(self, index):
        current_index = index
        
        while current_index > 0:
            parent_index = self._get_parent_index(current_index)
            
            if self.data[current_index] < self.data[parent_index]:
                self.data[current_index], self.data[parent_index] = \
                    self.data[parent_index], self.data[current_index]
                
                current_index = parent_index
            else:
                break

    def _heapify_down(self, index):
        current_index = index
        data_length = len(self.data)

        while True:
            left_index = self._get_left_child_index(current_index)
            right_index = self._get_right_child_index(current_index)
            smallest_index = current_index

            
            if left_index is not None and self.data[left_index] < self.data[smallest_index]:
                smallest_index = left_index

            if right_index is not None and self.data[right_index] < self.data[smallest_index]:
                smallest_index = right_index

            if smallest_index != current_index:
                self.data[current_index], self.data[smallest_index] = \
                    self.data[smallest_index], self.data[current_index]
                
                current_index = smallest_index
            else:
                break







class Patient:
    def __init__(self, name, urgency):
        if not isinstance(name, str) or not name:
            raise ValueError("Patient name must be a non-empty string.")
        if not isinstance(urgency, int) or urgency < 1:
            raise ValueError("Urgency must be a positive integer.")
        self.name = name
        self.urgency = urgency

    def __lt__(self, other):
        return self.urgency < other.urgency

    def __repr__(self):
        return f"Patient(name='{self.name}', urgency={self.urgency})"

class EmergencyQueue:

    def insert(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient objects can be inserted into the queue.")
            
        self.data.append(patient)
        
        self._heapify_up(len(self.data) - 1)
        print(f"INSERTED: {patient.name} (Urgency: {patient.urgency})")

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]
        
    def remove_min(self):
        if self.is_empty():
            return None

        if len(self.data) == 1:
            removed_patient = self.data.pop()
            print(f"REMOVED: {removed_patient.name} (Urgency: {removed_patient.urgency}) - Last one!")
            return removed_patient

        removed_patient = self.data[0]
        
        self.data[0] = self.data.pop()
        
        self._heapify_down(0)
        
        print(f"REMOVED: {removed_patient.name} (Urgency: {removed_patient.urgency}) - Treated and released!")
        return removed_patient

    def print_heap(self):
        if self.is_empty():
            print("The emergency queue is empty.")
            return

        print("\n--- Current Emergency Queue (Priority Order) ---")
        for i, patient in enumerate(self.data):
            print(f"[{i:2}] {patient.name:<15} | Urgency: {patient.urgency}")
        print("---------------------------------------------")


if __name__ == "__main__":
    
    
    queue = EmergencyQueue()
    
    p_urgent = Patient("Mr. Smith (Stroke)", 1)
    p_broken = Patient("Ms. Jones (Broken Leg)", 4)
    p_cold = Patient("Bobby (Common Cold)", 10)
    p_bleeding = Patient("Gary (Severe Bleeding)", 2)
    p_asthma = Patient("Karen (Asthma Attack)", 3)

    print("\n--- Insertion Test ---")
    
    queue.insert(p_broken)   # Urgency 4
    queue.insert(p_cold)     # Urgency 10
    queue.insert(p_urgent)   # Urgency