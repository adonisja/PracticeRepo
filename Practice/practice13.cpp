#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/*  Producing the Sum and Average of an array of grades using a Do...While loop
*/

#include <iostream>
using namespace std;

int main()
{
    const int SIZE = 3;
    int grade[SIZE], sum = 0;
    for (int i = 0; i < SIZE; i++)
    {
        do
        {
            cout << "Please enter grade: " << i + 1 << ": ";
            cin >> grade[i];
            if (grade[i] < 1 || grade[i] > 5)
            {
                cout << "Invalid grade! Enter a grade between 1 and 5 \n";
            }
        } while (grade[i] < 1 || grade[i] > 5);
        sum += grade[i];
    }
    
    cout << "Sum of ";
    for (int i = 0;i < 3;i++)
    {
        if (i < 2)
        {
            cout << grade[i] << " + ";
        }
        else
        {
            cout << grade[i];
        }
        
    } 
    cout << " = " << sum << endl;
    cout << "Average grade = " << (float)sum / SIZE << endl;
    return 0;
}