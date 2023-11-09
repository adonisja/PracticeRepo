#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
using namespace std;

/*
*/

#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
using namespace std;

class Queue
{
private:
    class Node
    {
    private:
        int data;
        class Node 
        {
            public:
            int value; // data stored in the node
            Node *next; // pointer to the next node in the list
            Node(int data) {
                this->value = data;
                next = nullptr;
            }
        };
        Node *head;
        Node *tail;
        
        bool IsEmpty()
        {
            return (head == NULL);
        }

        int Peek()
        {
            return head.data;
        }
    };
    public:
    Queue()
    {
        
    }
        ~Queue()
        {
            
        }
};
int main()
{
    Queue q;
    return 0;
}
