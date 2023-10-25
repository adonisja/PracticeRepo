#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
#include <list>
using namespace std;

class YoutubeChannel //class definition
{
    private:
        string name;
        string ownername;
        int subCount;
        
    
    public:
        list<string> publishedVidTitles;
        YoutubeChannel(string Name, string Ownername) 
    /* Constructor definition, a constructor is invoked everytime a new object is created for the class
        Rules: 
            A constructor has the same name as the class
            A constructor has no return type
    */
        {
            name = Name;
            ownername = Ownername;
            subCount = 0;

        }
        void Subscribe()
        {
            subCount++;
        }

        void UnSubscribe()
        {
            if (subCount > 0)
            {
            subCount--;
            }
        }

        void GetInfo() //Class Method: defines the behaviour of a class
        {   
            char ans;
            cout << "Channel Name: " << name << endl;
            cout << "Owned by: " << ownername << endl;
            cout << "Videos are: " << endl;
            for (string VideoTitle : publishedVidTitles)
            {
                cout << VideoTitle << endl; 
            }
            do{
                cout << "Would you like to Subscribe? Y/N: " << endl;
                cin >> ans;
                if (ans == 'Y' || ans == 'y')
                {
                    Subscribe();
                }
            } while (ans != 'Y' && ans != 'N' && ans != 'y' && ans != 'n' );
            do{
                cout << "Would you like to UnSubscribe? Y/N: " << endl;
                cin >> ans;
                if (ans == 'Y' || ans == 'y')
                {
                    UnSubscribe();
                }
            } while (ans != 'Y' && ans != 'N' and ans != 'y' and ans != 'n');
            cout << "Subscriber Count: " << subCount << endl << endl;
        }

        string GetName() const
        {
            return name;
        }

        void SetName(const string& newName)
        {
            name = newName;
        }

        string GetOwnerName()
        {
            return ownername;
        }

        void SetOwnerName(const string& newOwnername)
        {
            ownername = newOwnername;
        }
};

int main()
{
    string name;
    string ownername; // Define the variable "ownername"
    cout << "What is the name of this channel? ";
    getline(cin, name);
    cout << "Who owns " << name << "? ";
    getline(cin, ownername);
    YoutubeChannel ytube(name, ownername); // Object definition
    ytube.publishedVidTitles.push_back("C++ for Beginners"); //push_back adds an element at the end of the "publishedVidTitles" list
    ytube.publishedVidTitles.push_back("Coding Practice 101");
    ytube.GetInfo(); // Call for the Class Method "GetInfo()"
    
    cout <<"This is channel 2: " << endl;
    cout << "What is the name of this channel? ";
    getline(cin, name); //allows for string input that includes spaces
    cout << "Who owns " << name << "? ";
    getline(cin, ownername);
    YoutubeChannel ytube2(name, ownername);
    ytube2.publishedVidTitles.push_back("Biology 101");
    ytube2.publishedVidTitles.push_back("Biology for Dummies");
    ytube2.GetInfo();

    
}