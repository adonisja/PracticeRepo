#include <iostream>
#include <climits>
using namespace std;

int main()
{
    /* this accepts a number and outputs it
    int num1;

    cout << "Hello, this is my first test\n";
    cout << "Enter a number: ";
    cin >> num1; 
    cout << num1 << "\n";   */

    //This will output the size of numerous datatypes
    cout << "The size of int is: " << sizeof(int) << "\n";
    cout << "The size of double is: " << sizeof(double) << "\n";
    cout << "The size of long is: " << sizeof(long) << "\n";
    cout << "The size of char is: " << sizeof(char) << "\n";
    cout << "The size of string is: " << sizeof(string) << "\n";
    cout << "The size of bool is: " << sizeof(bool) << "\n";
    cout << "This will output the lowest possible value of an int variable: " << INT_MIN << "\n";
    cout << "This will output the highest possible value of an int variable: " << INT_MAX << "\n";
}