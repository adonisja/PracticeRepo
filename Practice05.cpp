#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
using namespace std;

/* A Number Guessing Game
    a precursor to a Hangman Game */
int main()
{
    int hostNum = 0, guestNum = 0, guestCount = 5;
    cout << "Welcome Host! Please Enter a number: " << "\n";
    cin >> hostNum;
    system("cls");
    cout << "Welcome Guest! Can you guess the number entered by the Host?\n";
    cout << "You have " << guestCount << " attempts\n\n";
    cout  << "Enter your first guess: ";
    cin >> guestNum;
    while (guestNum != hostNum)
    {
        guestCount--;
        cout << "\n\nSorry, you did not guess the correct number, please try again: ";
        cin >> guestNum;
        
        if (guestCount > 0 && guestNum != hostNum)
        {
            cout << "\nYou have: " << guestCount << " remaining\n";
        }
        else if (guestCount <= 0 && guestNum != hostNum)
        {
            cout << "Im sorry \nYou have used up of all your attempts\n";
            break;
        }
    }
    if (guestNum == hostNum)
    {
        cout << "Congratulations! You have correctly guessed the number!\n\n";
    }


    /* Ternerary Operator
    (guestNum == hostNum)? cout << "Correct!" : cout << "Failed";
    (condition)     ?ternary operator, if true execute : if false executes this section
    */


    return 0;
}