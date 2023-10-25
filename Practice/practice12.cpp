#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/* Program for calculating the Factorial
*/

int main()
{
    int num, factorial = 1;
    cout << " Enter a number to calculate the facorial: ";
    cin >> num;
    for (int i = 1; i <= num; i++)
    {
        factorial *= i;
    }
    cout << num <<  "! = " << factorial << endl;
    return 0;
}