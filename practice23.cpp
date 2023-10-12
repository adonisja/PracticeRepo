#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
using namespace std;

/* Recursive Functions. -- Intermediate Level
    - A function that calls itself
    - Must have a base case
    - Must have a recursive case
    - Must change its state and move toward the base case
*/

template <class T>
void Swap(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}


int recursiveSum(int a, int b)
{
    if (a == b) //base case, prevents infinite loop, returns the value of a when a == b
    {
        return a;
    }
    return a + recursiveSum(a + 1, b);
}

int main()
{
    int a, b;
    cout << "Enter a number: ";
    cin >> a;
    cout << "Enter another number: "; 
    cin >> b;
    if (a > b)
    {
        Swap<int>(a, b);
    }
    cout << "The sum of all numbers between " << a << " and " << b << " is: " << recursiveSum(a, b) << endl;
    return 0;
}