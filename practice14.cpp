#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/* A Program to print a multiplication times table
*/

int main()
{   
    cout << "Multiplication Times Table:" << endl;
    for (int i = 1;i < 15;i++)
    {
        for (int x = 1;x <= 12; x++)
        {
            cout << i << " * " << x << " = " << i*x << endl;
        }
        cout << "--------------------" << endl;
    }
    return 0;
}