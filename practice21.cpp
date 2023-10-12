#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
using namespace std;

/* Building an ATM (Beginner's Version)
    Functions Needed: Check Balance, Deposit Money, Withdraw Money, Pin Verification, Show Menu
*/
bool checkPin();
void checkBalance(long balance);
long withdrawCash(long balance);
long depositCash(long balance);
void showMenu();

void showMenu()
{   
    cout << "**** Welcome to XYZ Bank ****" << endl;
    int option, choice;
    long balance = 200.00;
    do 
    {
        cout << "1. Check Balance" << endl;
        cout << "2. Withdraw Cash" << endl;
        cout << "3. Deposit Cash" << endl;
        cout << "4. Exit" << endl;
        cout << "*********************" << endl;
        cin >> option;
        cout << endl;
        if (option == 1)
        {
            //cout << "Your remaining balance is: " << balance <<endl;
            checkBalance(balance);
            cout << "Would you like to continue?" << endl;
            cout << "1. Yes" << endl << "2. No" << endl;
            cout << "Your response: ";
            cin >> choice;
            cout << endl;
            if (choice == 2)
            {
                break;
            }
        }
        else if (option == 2) 
        {
            balance = withdrawCash(balance);
            cout << "Would you like to continue?" << endl;
            cout << "1. Yes" << endl << "2. No" << endl;
            cout << "Your response: ";
            cin >> choice;
            cout << endl;
            if (choice == 2)
            {
                break;
            }
        }
        else if (option == 3) 
        {
            balance = depositCash(balance);
            cout << "Would you like to continue?" << endl;
            cout << "1. Yes" << endl << "2. No" << endl;
            cout << "Your response: ";
            cin >> choice;
            cout << endl;
            if (choice == 2)
            {
                break;
            }
        }
        else if (option == 4) 
        {
            cout << "Thank You. Goodbye!" << endl;
            break;
        }
        else
        {
            cout << endl << "Invalid Option, Please choose from the Menu below: " << endl;
        }
    } while (option != 4);
}

bool checkPin()
{
    int userPin = 1234, pin, attempts = 3;
    bool pinFlag = false;
    do
    {
        cout << "Please Enter Your PIN: ";
        cin >> pin;
        if (pin == userPin)
        {
            break;
        }
        else
        {
            attempts -= 1;
            cout << "\nYou entered an incorrect PIN!" << endl;
            cout << "You have: " << attempts << " attempts remaining." << endl;
        }
    } while (attempts > 0);

    if (attempts == 0)
    {
        cout << "All attempts have been used!" << endl <<"Your Account is now blocked!" << endl;
    }
    else
    {
        cout << "You have entered the correct PIN." << endl << endl;
        pinFlag = true;
    }
    return pinFlag;
}

void checkBalance(long balance)
{
    std::cout << endl << "Your remaining balance is: $" << std::setprecision(2) << balance << endl;
}

long withdrawCash(long balance)
{
    float withdraw;
    cout << "Enter the Withdrawal Amount: $";
    cin >> withdraw;
    if (withdraw > balance)
    {
        cout << "Insufficient Funds" << endl;
        checkBalance(balance);
    }
    else
    {
        balance -= withdraw;
        checkBalance(balance);
    }
    return balance;
}

long depositCash(long balance)
{
    long deposit;
    cout << "Enter your deposit amount: $";
    cin >> deposit;
    balance += deposit;
    checkBalance(balance);
    return balance;
}

int main()
{
    bool pin;
    pin = checkPin();
    if (pin)
    {
        showMenu();
    }
    else
    {
        cout << "Transaction Terminated" << endl;
    }
    return 0;
}