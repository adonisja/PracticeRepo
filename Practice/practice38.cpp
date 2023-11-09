#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
using namespace std;

/* A program to sort numbers entered in an array
*/

int findSmallest(int myArray[], int *size, int sortedArray[])
{
    int smallest;

    for (int count = *size; count > 0; count--)
    {
            if (myArray[count] < myArray[count-1])
            {
                smallest = myArray[count];
            }
    }
    return smallest; 
}


int main()
{
    int size;
    int *myArray = new int [size];
    int *sortedArray = new int [size];
    cout << "How many numbers are there to be sorted? ";
    cin >> size;
    for (int count = 1; count <= size; count++)
    {
        cout << "Number " << count << ": ";
        cin >> myArray[count-1];
    }
    cout << "The original numbers are: \n {";
    for (int count = 0; count < size; count ++)
    {
        if ((count+1) < size)
        {
            cout << myArray[count] << ", ";
        }
        else
        {
            cout << myArray[count] << "} \n";
        }  
    }
    sortedArray[0] = findSmallest(myArray, &size, sortedArray);
    for (int i = 1; i < size; i++) 
    {
        sortedArray[i] = sortedArray findSmallest(myArray, &size, sortedArray+i-1);
    }
    cout << "Sorted numbers are: {";
    for (int count = 0; count < size; count ++)
    {
        if ((count+1) < size)
        {
            cout << sortedArray[count] << ", ";
        }
        else
        {
            cout << sortedArray[count] << "} \n";
        }  
    }


    return 0;
}
