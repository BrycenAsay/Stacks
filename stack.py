"""mainly just creates a stack ADT""" 
class Stack:
    """Stack ADT"""
    def __init__(self):
        self.head = None
    def push(self,item):
        """pushes an item onto the stack"""         
        new_item = Node(item)
        new_item.next = self.head
        self.head = new_item
    def pop(self):
        """takes the top item off the stack and returns it"""         
        if self.head is None:
            raise IndexError
        copy = self.head
        self.head = self.head.next
        return copy.data
    def top(self):
        """returns the top value without removing it"""         
        if self.head is None:
            raise IndexError
        return self.head.data
    def size(self):
        """returns the size of the stack"""         
        curr = self.head
        num_of_items = 0
        while curr is not None:
            num_of_items += 1
            curr = curr.next
        return num_of_items
    def clear(self):
        """clears the entire stack"""         
        self.head = None
    def isempty(self):
        """tests wether the stack is empty or not"""         
        if self.head is None:
            return True
        else:
            return False
    def print_vals(self):
        """prints all values in the stack"""         
        curr = self.head
        while curr is not None:             
            print(curr.data)
            curr = curr.next

class Node:
    """defines a class Node for objects in stack"""     
    def __init__(self,data):
        self.data = data
        self.next = None

def main():
    yes = Stack()
    yes.push('good')
    yes.push('is')
    yes.push('mom')
    yes.push('your')
    print(yes.top())
    yes.pop()
    print(yes.top())
    yes.print_vals()
    print(yes.size())
    yes.clear()
    yes.push('yay')
    yes.push('it emptied')     
    yes.print_vals()

if __name__ == '__main__':
    """runs if this is the file being ran"""     
    main()