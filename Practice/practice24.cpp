#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
using namespace std;

/* Calulating the factorial of a number using Recursive Functions */

int factorial(int n)
{
    if ( n == 0)
    {
        return 1;
    }
    return n * factorial(n - 1);
}

int main()
{
    int n;
    cout << "Enter a number to calculate the factorial: ";
    cin >> n;
    cout << n << "! is " << factorial(n) << endl;
    return 0;
}