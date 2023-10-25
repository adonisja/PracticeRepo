#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/* Function Overloading: There are 3 definitions for the function "Sum" each accepting and returning different
data types, this is an example of function overloading, where there can be multiple definitions of a 
function sharing the same name.
*/

int Sum(int a, int b);
double Sum(double a, double b);
float Sum(float a, float b);

int main()
{
    float num1, num2;

    cout << "Enter a number: ";
    cin >> num1;
    cout << "Enter another number: ";
    cin >> num2;
    cout << "The sum of " << num1 << " and " << num2 << ": " << Sum(num1, num2) << endl;
    
    return 0;
}

int Sum(int a, int b)
{
    return a+b;
}

double Sum(double a, double b)
{
    return a+b;
}

float Sum(float a, float b)
{
    return a+b;                        
}