#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
#include <list>
using namespace std;

/*  Void Pointers: A pointer that can hold the address of a variable of any other datatype
        Limitation: A void pointer cannot be directly dereferenced. 
            (i.e.: void *ptr cannot be dereferenced as ptr = ... later or ... = ptr 
*/

void PrintNum(int *numPtr)
{
    cout << "*numPtr: " << *numPtr << endl;
}

void PrintLetter(char *charPtr)
{
    cout << "*charPtr: " << *charPtr << endl;
}

void Print(void *ptr, char type)
{
    switch (type)
    {
        case 'i' :  cout << *((int*)ptr) << endl; //Recasts the pointer(ptr) inherited as a void pointer into an int pointer and prints it
                    break;

        case 'c' : cout << *((char*)ptr) << "\n"; //Recasts the pointer(ptr) inherited as a void pointer into an char pointer and prints it
                    break;

        case 'f' : cout << *((float*)ptr) << endl;//Recasts the pointer(ptr) inherited as a void pointer into an floar pointer and prints it
                    break;

        case 'b' : cout << *((bool*)ptr) << endl;//Recasts the pointer(ptr) inherited as a void pointer into an bool pointer and prints it
                    break;
    }
}

int main()
{
    int num = 5;
    PrintNum(&num);
    char letter = 'a';
    PrintLetter(&letter);
    Print(&num, 'i');
    Print(&letter, 'c');
    cout << "type of num is: " << typeid(num).name() << endl;
    cout << "type of char is: " << typeid(char).name() << endl;
    //typeid(variable).name(); returns the type of the variable passed as a single character, e.g typeid(num).name() is 'i'
    return 0;
}