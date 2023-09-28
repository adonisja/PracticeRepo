#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/* This program will output the values between 100-500 that
    are divisible by both 3 and 5
*/

int main()
{
    int counter = 100;
    while (counter < 500)
    {
        if (counter%3 == 0 && counter%5 == 0)
        {
            cout << counter << "\n";
        }
        counter++;
    }

    return 0;
}