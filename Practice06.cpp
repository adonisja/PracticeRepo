#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
    float num1, num2;
    char operation;
    cout << "Enter your first number: ";
    cin >> num1;
    cout << "Enter your second number: ";
    cin >> num2;
    cout << "Enter the operation your wish to do: ";
    cin >>  operation; 

    switch (operation)
    {
    case '+':
        cout << "\n" << num1 << operation << num2 << "is: " << num1 + num2 << "\n";
        break;
    
    case '-':
        cout << "\n" << num1 << operation << num2 << "is: " << num1 - num2 << "\n";
        break;
    case '*':
        cout << "\n" << num1 << operation << num2 << "is: " << num1 * num2 << "\n";
        break;
    case '/':
        cout << "\n" << num1 << operation << num2 << "is: " << num1 / num2 << "\n";
        break;
    case '%':
        bool isNum1Int, isNum2Int;
        isNum1Int = ((int)num1 == num1);
        isNum2Int = ((int)num2 == num2);
        if (isNum1Int && isNum2Int)
        {
            cout << num1 << operation << num2 << " = " << (int)num1%(int)num2;
        }
        else
        {
            cout << "This operation is not valid!" << "\n";
        }
        break;
    case '^':
        cout << num1 << operation << num2 << " = " << pow(num1, num2) << "\n";
        break;
    
    default:
        cout << "Not a valid operation";
        break;
    }
    return 0;
}