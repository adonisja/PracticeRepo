#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
using namespace std;

/* MultiDimensional Dynamic Array
*/

int main()
{
    int rows, columns;
    cout << "Enter how many rows: ";
    cin >> rows;
    cout << "Enter how many columns: ";
    cin >> columns;
    //Memory allocation
    int **table = new int *[rows]; //Creates a table of pointers that points to the addresses of each row
    for (int i = 0; i < rows; i++)
    {
        //for each row, create a new column until the max columns requested by the user and store the address
        table[i] = new int [columns];   
    }
    table[1][2] = 88;
    //Deallocate memory
    for (int i = 0; i < rows; i++)
    {
        delete [] table[i]; 
    }
    delete [] table;
    table = NULL;
    return 0;
}
