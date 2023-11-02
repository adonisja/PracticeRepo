#include <iostream>
using namespace std;

int main()
{
    int luckynumbers[5] = {1, 2, 3, 4, 5};
   /* cout << luckynumbers << endl;
    cout << &luckynumbers[0] << endl;
    cout << luckynumbers[2] << endl;
    cout << *(luckynumbers + 2) << endl; // *is the dereference operator */
    for (int i = 0; i < 5; i++)
    {
        cout << "Enter a number: ";
        cin >> luckynumbers[i];
    }
    for (int i = 0; i < 5; i++)
    {
        cout << "Value stored in " << &(luckynumbers[i]) << " is: " << *(luckynumbers + i) << endl; 
    } 
    return 0;
}
