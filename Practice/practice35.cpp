#include <iostream>
using namespace std;

class Node
{
    public:
        int value;
        Node *next;
};

void printList(Node *n)
{
    while (n != NULL)
    {
        cout << n->value << endl;
        n = n->next;
    }
}

void insertAtFront(Node**head, int newValue)
{
    /* Three things to do:
        Create a new node
        Put it at the front of the linked list
        Move head of the list to point to this new node
    */

    Node *newNode = new Node();
    newNode->value = newValue;
    newNode->next = *head;
    *head = newNode;
       
}

void insertAtEnd(Node**head, int newValue)
{
    /*Things to do:
        Create a new node
        Check if list is empty
        Traverse the linked list until the end
        Put new Node to the end
        Link previous node to new node
        Set new node next to NULL  
    */
   Node *newNode = new Node();
   newNode->value = newValue;
   newNode->next = NULL;
   if (*head == NULL)
   {
        *head = newNode;
        return;
   }
   Node *temp = *head;
   while (temp->next != NULL)
   {
        temp = temp->next;
   }
   temp->next = newNode;
}

void insertAfter(Node *previous, int newValue)
{
    /* Things to do:
        Check if previous value is NULL
        Prepare a new Node
        Insert new Node after previous
    */
   if (previous == NULL)
   {
        cout << "previous cannot be NULL" << endl;
        return;
   }
   Node *newNode = new Node();
   newNode->value = newValue;
   newNode->next = previous->next;
   previous->next = newNode;
}

int main()
{
    Node *head = new Node();
    Node *second = new Node();
    Node * third = new Node();
    Node *fourth = new Node();

    head->value = 1;
    head->next = second;
    second->value = 2;
    second->next = third;
    third->value = 3;
    third->next = fourth;
    fourth->value = 4;
    fourth->next = NULL;
    cout << "Original List: " << endl;
    printList(head);
    insertAtFront(&head, -1);
    cout << "Insert at Head: " << endl;
    printList(head);
    insertAtEnd(&head, 5);
    cout << "Insert at End: " << endl;
    printList(head);
    insertAfter(head, 0);
    cout << "Insert at a Given Node: " << endl;
    printList(head);


    return 0;
}