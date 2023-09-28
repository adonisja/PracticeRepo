#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/* A PIN checker Program 
    using a Do...While loop
*/

int main()
{
    int userPin = 1234, pin, attempts = 3;
    do
    {
        cout << "Enter Your PIN: ";
        cin >> pin;
        if (pin == userPin)
        {
            break;
        }
        else
        {
            attempts -= 1;
            cout << "\nYou entered an incorrect PIN!\n";
            cout << "You have: " << attempts << " remaining.\n";
        }
    } while (attempts > 0);

    if (attempts == 0)
    {
        cout << "All attempts have been used!\nYour Account is blocked!\n";
    }
    else
    {
        cout << "You have entered the correct PIN. \n";
    }

    return 0;
}