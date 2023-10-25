#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
using namespace std;

/* Introduction to Generic Functions
*/

// Intermediate level 

template <typename T> //this must preceed the use of the T data type before the function definition
void Swap(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}


int main()
{
    int a, b;
    cout << "Enter a number: ";
    cin >> a;
    cout << "Enter another number: ";
    cin >> b;
    cout << "Before swapping: " << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    Swap<int>(a, b);
    cout << "After swapping: " << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    return 0;
}