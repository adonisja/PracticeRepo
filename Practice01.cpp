#include <iostream>
#include <climits>
#include <array>
using namespace std;

int main()
{
    // this accepts a number and outputs it
    float num[] = {0}, sum = 0, avg = 0;
    int count = 0, numSize = 0, i = 0;

    //This will accept a list of numbers and find the average between them
    cout << "Enter a list of numbers or 0 to end: ";
    cin >> num[0];
    
    while (num[i] != 0)
    {
        sum = sum + num[i];
        count = count +=1;
        cout << "Enter the next number or 0 to end: ";
        cin >> num[i];
    } 
   // cout << "The sum of the numbers is: " << sum << "\n"; 
   // cout << "The count of the numbers is: " << count << "\n";    
    avg = sum / count;
   //cout << "The average of the numbers is: " << avg << "\n";
    numSize = sizeof(num); //This calculates the size of the array
    cout << "The size of the array is: " << (numSize - 1) << "\n";

    cout << "The average of: \n";
    for(int a = 0; a < numSize; a += 1)
    {
        cout << num[a] << ", ";
    }
    cout << "\nis: " << avg;


    //This will output the size of numerous datatypes
    /*
    cout << "The size of int is: " << sizeof(int) << "\n";
    cout << "The size of double is: " << sizeof(double) << "\n";
    cout << "The size of long is: " << sizeof(long) << "\n";
    cout << "The size of char is: " << sizeof(char) << "\n";
    cout << "The size of string is: " << sizeof(string) << "\n";
    cout << "The size of bool is: " << sizeof(bool) << "\n";
    cout << "This will output the lowest possible value of an int variable: " << INT_MIN << "\n";
    cout << "This will output the highest possible value of an int variable: " << INT_MAX << "\n";
    */
}