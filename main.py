class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_sorted(self, new_data):
        new_node = Node(new_data)
        if self.head is None or self.head.data >= new_data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < new_data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def print_heights(self):
        current = self.head
        while current:
            feet = current.data // 12
            inches = current.data % 12
            print(f"{int(feet)} feet {int(inches)} inches")
            current = current.next

    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next #moves fast pointer twice as fast as slow pointer so when fast is at the end the slow will be in the middle
        return slow_ptr.data
    
    def print_reverse(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            self._print_reverse_recursive(self.head)
    
    def _print_reverse_recursive(self, node):
        if node is None:
            return
        self._print_reverse_recursive(node.next)
        print(node.data)
display = [] #list to show inputs as they are being listed
#function to input heights from the user
def input_heights():
    i = 1
    w = True
    heights = []#real list that gets used later
    
    while w:
        print(display)
        height_str = input(f"Enter height in ft and inches seperated by an apostrophe (5'7). Then press 'enter'. type 'done' when finished.\n   Height {i}: ")
        i= i+1
        
        if height_str.lower() == 'done':
            w = False
            break
        try:
            feet, inches = height_str.split("'")
            feet = int(feet)
            inches = float(inches)
            display.append(height_str)
            display.sort()
            if feet >= 0 and 0 <= inches < 12:
                total_inches = feet * 12 + inches
                heights.append(total_inches)
            else:
                print("Invalid height. Please enter a valid height.")
        except ValueError:
            print("Invalid input format. Please enter height in feet plus inches (Ex: 5'11 or 5'3).")
    return heights
heights_in_inches = input_heights()#take inputs and put them in linked list
llist = LinkedList()#create a linked list of student heights
Llist = LinkedList()
for Height in display:
    Llist.insert_sorted(Height)
for height in heights_in_inches:
    llist.insert_sorted(height)
Risplay = display
Risplay.sort(reverse= True)
print("All heights from tallest to shortest:")
#print(Risplay)
Llist.print_reverse()
#llist.print_heights()#print all heights in ascending order
#find the middle height then convert from inches to ft + in
middle_height = llist.find_middle()
middle_height_feet = middle_height // 12
middle_height_inches = middle_height % 12
#function to make it so feet doesnt show up as 5.0 and 5 inches
middle_height_feet = int(middle_height_feet)
#prints the moddle height in feet and inches
print(f"\nThe middle student height is: {middle_height_feet} feet {middle_height_inches} inches") 
