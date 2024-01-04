#include <iostream>
#include <iomanip>
#include <stack>


void ArrayInitializer()
{
    //creates a seed for the random number generator function based on current time when program is run
    srand((unsigned) time(NULL));
    int numList[9];
    int reversedNumList[9];
    int reversedCount = 9;
    //initializes the initial array with 
    for (int count = 0; count < 10; count++)
    {
        numList[count] = rand(); //creates an array to store random numbers
        reversedNumList[reversedCount] = numList[count]; //initializes another array with the previous array in reversed order
        reversedCount--;
    }
    std::cout << "Initial Array  \n";
    for (int count = 0; count < 10; count++)
    {
        std::cout << "Array [" <<count+1 << "]: " << numList[count] << "\n";
    }
    std::cout << "\nReversed List is: \n";
    for (int count = 0; count < 10; count++)
    {
        std::cout << "Array [" <<count+1 << "]: " << reversedNumList[count] << "\n";
    }
}

bool checkPalindrome()
{
    std::string word;
    std::cout << "Enter a palindrome";
    std::cin >> word;
    


}

int main()
{
    ArrayInitializer();
}