#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/* A Program to Determine if a number is a Prime Number: Intro on Return types
*/
bool isPrime(int num);

int main()
{
    int num, count = 0;
    bool prime;

    /* cout << "Enter a number: ";
    cin >> num; */

    for (int i = 0; i < 1000; i++)
    {
        prime = isPrime(i);
        if (prime)
        {
            cout << i << " is a prime number." << endl;
            count++;
        }
    }
    cout << "There are " << count << " prime numbers between 1 and 1000" << endl;
    /*prime = isPrime(num);
    if (prime)
    {
        cout << num << " is a prime number." << endl;
    }
    else
    {
        cout << num << " is not a prime number." << endl;
    } */
    return 0;
}

bool isPrime(int num)
{
    bool prime = true; 
    for (int x = 2; x < num;x++)
    {
        if (num % x == 0)
        {
            prime = false;
            break;
            //return false; Can replace this entire section of code
        }
    }
    return prime;
}