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
    int height, width;
    char symbol;
    cout << "Enter the Height: ";
    cin >> height;
    cout << "Enter the width: ";
    cin >> width;
    cout << "Enter the symbol to construct the shape: ";
    cin >> symbol;
    for (int i = 0; i <= height; i++)
    {
        for(int a = 0; a <= width; a++)
        {
            cout << setw(3) << symbol; //setw manipulates the width of the fields, it is included in the iomanip library
        }
        cout << endl;
    }

    return 0;
}