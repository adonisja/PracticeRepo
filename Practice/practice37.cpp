#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
using namespace std;

/* Dynamic Arrays

    Note: * is a pointer, it indicates that this variable "points" to another actual
          & is a reference for the address of the variable
          ** is a double pointer, it indicates that this variable "points" to a pointer of another variable
*/

void getMinAndMax(int myArray[], int *size, int *min, int *max, int *minIndex, int *maxIndex)
{
    for (int i = 1; i < *size; i += 1)
    {
        if (myArray[i] < *min)
        {
            *min = myArray[i];
            *minIndex = i;
        }
        if (myArray[i] > *max)
        {
            *max = myArray[i];
            *maxIndex = i;
        }
    }
}


int main()
{
    int size;
    cout << "What is the size of your array? ";
    cin >> size;
    int *myArray = new int [size]; //Creates a new integer array of size
    int min = myArray[0], max = myArray[0];
    int minIndex = 0, maxIndex = 0;
    for (int i = 0; i < size; i += 1)
    {
        cout << "Array[" << i <<"]: " ;
        cin >> myArray[i];
    }
    for (int i = 0; i < size; i += 1)
    {
        cout << "{"<< myArray[i] << "} ";
    }
    cout << endl;
    getMinAndMax(myArray, &size, &min, &max, &minIndex, &maxIndex);
    cout << "The min variable is Array[" << minIndex << "] : " << min << endl;
    cout << "The max variable is Array[" << maxIndex << "] : " << max << endl;
    return 0;

}
