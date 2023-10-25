#include <iostream>
#include <climits>
#include <array>
using namespace std;

int main()
{
    //Program to Swap Two Numbers
    int a = 10, b = 20, temp = 0;
    cout << "The value of a is: " << a << "\n";
    cout << "The value of b is: " << b << "\n\n";
    temp = a;
    a = b;
    b = temp;
    cout << "After swapping: \n";
    cout << "The value of a is: " << a << "\n";
    cout << "The value of b is: " << b << "\n\n";

    //Additional Method to Swap Two Numbers without using a third variable
    int c = 10, d = 20;
    cout << "The value of c is: " << c << "\n";
    cout << "The value of d is: " << d << "\n\n";
    c = c + d;
    d = c - d;
    c = c - d;
    cout << "After swapping: \n";
    cout << "The value of c is: " << c << "\n";
    cout << "The value of d is: " << d << "\n\n";

    return 0;
}