#include <iostream>
using namespace std;

/*  Linked Lists:
        Each element in a linked list stores two things: the value stored in that node and the address of the next element
         in the list.
        The last element in the linked list stores the value of that element and a "NULL" variable to mark that
         there are no other elements in the list.
    Advantages: Linked Lists have dynamic storage space
    Disadvantages: Random access to the linked list is not allowed
                    Linked Lists require more memory

*/

class Node
{
    public:
        int value;
        Node *next;
};

void printList(Node *n)
{
    while(n != NULL)
    {
        cout << n->value << endl;
        n = n->next;
    }

};

int main()
{
    //Creating the Linked List
    Node *head = new Node();
    Node *second = new Node();
    Node *third = new Node();

    //Initializing the values and linking each node
    head->value = 1; 
    //-> is used to access members of a class when you are using pointers, it is used instead of the "." operator
    head->next = second;
    second->value = 2;
    second->next = third;
    third->value = 3;
    third->next = NULL;

    //Accessing the Linked List
    printList(head);

    return 0;
}