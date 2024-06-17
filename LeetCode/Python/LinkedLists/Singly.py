#Singly Linked List Example
class ListNode(object):
    def __init__(self, data):
        self.data = data # This is the data of the node
        self.next = None # This is the pointer to the next node

#creating a linked list

class SinglyLL:
    def __init__(self, data = 0):
        self.head = None # This is the head of the linked list
        self.data = data # This is the data of the linked list

    def Traversal(self):
        temp = self.head
        count = 1 
        # This is a temporary variable to traverse the linked list,
        # it starts from the head of the linked list
        if temp == None:
            print("Linked List is Empty")
        else:
            while temp:
                print(f'Node {count} = {temp.data}')
                count += 1
                temp = temp.next


    def InsertAtBeginning(self, value):
        new_node = ListNode(value)
        print(f"\nInserting {value} at the Beginning of Linked List: ")
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node


    def InsertAtEnd(self, value):
        new_node = ListNode(value)
        print(f'\nInserting {value} at the End of Linked List: ')
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    def InsertAtIndex(self, value, index):
        new_node = ListNode(value)
        print(f'\nInserting {value} at index {index}')
        count = 1
        temp = self.head
        if count == index:
            self.InsertAtBeginning(value)
        else:
            while (count != (index - 1)) and temp.next:
                count += 1
                temp = temp.next
                
            if count == (index - 1):
                new_node.next = temp.next
                temp.next = new_node
            else:
                print(f'Index {index} does not exist in the Linked List')

    def updateValueByIndex(self, value, index):
        temp = self.head
        new_node = ListNode(value)
        print(f"Updating Index {index} to the value {value}")
        count = 0
        if temp == None:
            print("This is an empty LL, there's nothing to update")
        while temp and (count != (index-1)):
            temp = temp.next
            count += 1
            print(f'Current Index: {count}')
            
        if count == index-1:
            print(value)
            temp.data = value
            print(temp.data)
            return
        else:
            print("Index not found")



    def AddNode(self, value):
        new_node = ListNode(value) # creates a new node
        if self.head == None:      # checks if the linked list is empty
            # assigns the new node to the head of the linked list if empty
            self.head = new_node   
        else:
            temp = self.head  # assigns the head of the linked list to a temporary variable
            
            while temp.next:  
                temp = temp.next
            temp.next = new_node # assigns the new node to the next pointer of the last node
        self.Traversal()
        return temp

    def removeFirstNode(self):
        if self.head == None:
            print("There nothing in the Linked List to remove")
        else:
            print(f'{self.head.data} was removed from the head of the Linked List')
            self.head = self.head.next
        self.Traversal()

    def removeLastNode(self):
        temp = self.head
        if self.head is None:
            print("There nothing in the Linked List to remove")
            return
        while temp.next.next:
            temp = temp.next
        print(f'{temp.next.data} is removed from the tail of the Linked List')
        temp.next = None
        self.Traversal()


    def RemoveNodeByValue(self, value):
        temp = self.head
        print(f"\nAttempting to remove {value}...")
       # Checking the head of the Linked List
        if temp.data == value:
            self.removeFirstNode()
        if temp is not None:
            print(f'Printing at \"is not None\" check {temp.data}')
            if temp.data == value:
                temp = temp.next
                print(f"Removed {value} from the head of the Linked List.")

        else:
            print("The Linked List is empty, cannot remove")
        self.Traversal()
         
            
    # Checking the other nodes
        while temp.next.next is not None and temp.next.data != value: 
            temp = temp.next

        if temp is not None:
            print("temp is not none")
            print(f'temp.data: {temp.data}')
            print(f'temp.next.data: {temp.next.data}')
            temp.next = temp.next.next
            print(f'{value} was found and removed')
            print(f'New temp.data: {temp.data}')
        else:
            print("temp is None")
            print(f'{value} was not found')
            return
        self.Traversal()
    
    def removeNodeByIndex(self, index):
        print(f"\n**Removing Node from index {index}**")
        temp = self.head
        count = 1
        if self.head == None:
            return
        if count == index:
            self.removeFirstNode()
        else:
            while temp and count != (index - 1):
                temp = temp.next
                count += 1
            if not temp:
                print("Index not Found!")
            if count == (index -1):
                print(f'{temp.next.data} was removed from the Linked List')
                temp.next = temp.next.next
        self.Traversal()

    
    def sizeOfLL(self):
        temp = self.head
        count = 0
        if self.head:
            while temp:
                count += 1
                temp = temp.next
            print(f'\nsize of Linked List = {count}')
            return count
        else:
            return 0


    def Sort(self):
        temp = self.head
        if temp == None:
            pass
            

def main():
    n1 = ListNode(3) # creating the first node
    sll = SinglyLL() # creating the linked list
    sll.head = n1    # assigning the head of the linked list to the first node
    n2 = ListNode(8) # creating the second node
    n1.next = n2     # linking the first node to the second node
    n3 = ListNode(7) # creating the third node
    n2.next = n3     # linking the second node to the third node
    n4 = ListNode(5) # creating the fourth node
    n3.next = n4     # linking the third node to the fourth node
    
    n5 = sll.AddNode(8)

    sll.InsertAtBeginning(2)
    
    sll.InsertAtEnd(10)
    
    sll.InsertAtIndex(11,3)
   
    sll.InsertAtIndex(13,10)

    sll.updateValueByIndex(12,4)
    
    sll.removeFirstNode()
    
    sll.removeLastNode()
    
    sll.RemoveNodeByValue(12)
    
    sll.removeNodeByIndex(4)
    size = sll.sizeOfLL()
    

if __name__ == "__main__":
    main()