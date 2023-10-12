#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/*
*/

int main()
{
    int height;
    char symbol;
    cout << "Enter height: ";
    cin >> height;
    cout << "Enter the symbol: ";
    cin >> symbol;
    for (int i = 1; i <= height; i++)
    {
        for (int a = 1; a <= i; a++)
        {
            cout << setw(4) << symbol;
        }
        cout << endl;
    }
    return 0;
}