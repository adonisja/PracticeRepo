#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/*  A Program that counts the digits in a given number
*/

int main()
{
    int num, num2, count = 0;
    cout << "Please enter a number: ";
    cin >> num;
    num2 = num;
    
    if (num == 0)
    {
        cout << "You have entered 0 \n";
    }
    else
    {
        if (num < 0)
        {
            num *= -1;
        }
        while (num > 0)
        {
            num /= 10;
            count += 1;
        }
    }
    cout << num2 << " contains: " << count << " digits. \n";
    return 0;
}