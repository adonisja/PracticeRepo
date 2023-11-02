#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
#include <list>
using namespace std;

/* Pointers: stores a memory location (address)
    "&" gives the address of the preceding variable.
    "*" denotes that the variable is a pointer that will hold an address reference.
    Pointer MUST be of the same type as the variable that it is pointing to.
*/

int main()
{
    int i = 5;
    cout << "i: " << i << endl;
    cout <<"&i: " << &i << endl;
    int *ptr = &i; //Initializes the ptr variable as a pointer and assigns the address of i to that pointer
    cout << "ptr: " << ptr << endl;
    cout << "*ptr: " << *ptr << endl; 
    /* Dereferences the address of the pointer, i.e.: it gives the value that is stored in the
    location (address) stored by the ptr variable.
    */
    *ptr = 10; //Changes the value that is stored at the address that ptr holds
    cout << "New *ptr: " << *ptr << endl;
    cout << "New i: " << i << endl;

    int v;
    int *ptr2 = &v;
    *ptr2 = 7;
    cout << "v: " << v << endl;
    return 0;
}