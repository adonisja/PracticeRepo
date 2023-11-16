/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode();  //Create a placeholder node "result"
        ListNode* ptr = result;     //Initialize a pointer that keeps track of the last node in the linked list 

        int carry = 0;  //carry will hold the digit to be carried 
        int digit = 0;  
        /* digit will be the remaining digit after finding the mod of the sum
         e.g.: if sum = 15
            digit = (sum = 15 % 10) = 5 
            and the carry = 1
        */
       // Create a while loop that checks if l1 is empty or l2 is empty or carry is not 0
        while (l1 != NULL || l2 != NULL || carry != 0)
        {
            /*Ternary operator that checks if l1/l2 is null, if it is NULL then the digit is set to 0,
                if not then the value stored is read and given to digit */
            int digit1 = (l1 != NULL) ? l1->val : 0; 
            int digit2 = (l2 != NULL) ? l2->val : 0;
            
            int sum = digit1 + digit2 + carry;

            carry = sum / 10;
            digit = sum % 10;
            
            /* Creates a new node that stores the resulting digit 
            and sets the tail of the node to this new node */
            ListNode* newNode = new ListNode(digit); 
            ptr->next = newNode;
            ptr = ptr->next;

            //Traverse the l1/l2 linked lists and obtain the next values for l1 & l2
            l1 = (l1 != NULL) ? l1->next : NULL;
            l2 = (l2 != NULL) ? l2->next : NULL;
        }
        //Return the final result by skipping the initial head node
        ListNode* finalResult = result->next;
        delete result;
        return finalResult;
    }
};