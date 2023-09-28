#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/*  A program to guess the amout of days in a given month
*/

int main()
{
    //leap year: (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)
    int year, month;
    cout << "Please enter the year you were born: ";
    cin >> year;
    cout << "Please enter your birth month in digits: ";
    cin >> month;

    switch (month)
    {
        case 2: (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) ?
            cout << "February has 29 days this leap year" : cout << "February has 28 days this year \n";
            break;
        /* the following case arguments will all execute until the program encounters the first 'break' so 2,3,6,9,11 will execute
        however, only case 11 has a code block, so it will execute this block for all previous switch case that did not have a 'beak'*/    
        case 4:
        case 6:
        case 9:
        case 11: cout << "This month has 30 days\n"; break;

        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12: cout << "This month has 31 days\n"; break;

        default: cout << "Invalid month entered.\n";
    }
    return 0;
}