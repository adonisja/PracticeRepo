#include <iostream>
#include <climits>
#include <array>
using namespace std;

int main()
{
    int counter = 0, counter2 = 0;  
    int a = 10, b = 20;   
    cout << counter++ << "\n"; //post increment operator: print then increment
    cout << ++counter2 << "\n\n"; // pre increment operator: increment then print

    // system("cls");  //clears the screen

    //Relational Operators: >, <, >=, <=, ==, !=
    cout << (a > b) << "\n"; //outputs 0 if false and 1 if true
    if (a < b)
    {
        cout << "a is less than b" << "\n\n";
    }
    else if (a > b)
    {
        cout << "a is greater than b" << "\n\n";
    }
    else
    {
        cout << "a is equal to b" << "\n\n";  
    }

    //Logical Operators: &&, ||, !

    cout << (a > b && a < b) << "\n"; //outputs 0 if false and 1 if true
    cout << "The value of a is: " << a << "\n";
    cout << "The value of b is: " << b << "\n";
    if (a > b && a < b)
    {
        cout << "a is greater than b and a is less than b" << "\n\n";
    }
    else if (a > b || a < b)
    {
        cout << "a is greater than b or a is less than b" << "\n\n"; 
    }
    else
    {
        cout << "a is equal to b" << "\n\n";  
    }       

    //
    //Bitwise Operators: &, |, ^, ~, <<, >>



    //Assignment Operators: =, +=, -=, *=, /=, %=, <<=, >>=, &=, ^=, |=


    //Ternary Operator: ?:


    //Order of Operators:
    /* Arithmetic: (), ++, --, *, /, %, +, -,
       Relational: <<, >>, <, <=, >, >=, ==, !=,
       Bitwise: &, ^, |,
       Logical: &&, ||, !,
        Ternary: ?:,
        Assignment: =, +=, -=, *=, /=, %=, <<=, >>=, &=, ^=, |=, ,
    return 0;
}


