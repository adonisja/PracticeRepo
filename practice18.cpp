#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
using namespace std;

/* Multiple Parameter Functions
*/
void introduceMe(string name, string city, int age); // The data type for each parameter must be stated

int main()
{
    string name, city;
    int age;

    cout << "what is your name? ";
    cin >> name;
    cout << "Where do you live? ";
    cin >> city;
    cout << "How old are you? ";
    cin >> age;
    cout << endl;

    introduceMe(name, city, age);
    
    return 0;
}

void introduceMe(string name, string city, int age)
{
    cout << "My name is " << name << endl;
    cout << "I live in " << city << endl;
    cout << "I am " << age << " years old." << endl;
}