#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/* A Program that reverses the digits of a given number
*/

int main()
{
    int num, num2, reversedNum = 0;
    cout << "Enter a number: ";
    cin >> num;
    num2 = num;
    while (num != 0)
    {
        reversedNum *= 10;
        reversedNum += num % 10;
        num /= 10;
    }
    if (num2 == 0)
    {
        cout << "You have entered 0 \n";
    }
    else
    {
        cout << num2 <<" reversed is: " << reversedNum << "\n";
    }
    return 0;
}