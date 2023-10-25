#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/* Functions Intro
*/
void function(); //Function declaration: return type function name(parameters)
/* A function declaration is necessary before the main function if the function definition comes after the main function in which it is called*/


int main() //Main function
{
    cout << "Hello from main() " << endl;
    function(); //function call
    return 0;
}

void function() //Function Definition
{
    cout << "Hello from function() " << endl;
}