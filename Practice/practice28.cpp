#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
#include <list>
using namespace std;

/*  Inheritance
*/

class YoutubeChannel //Class definition: YoutubeChannel is the main class for this program
{
    private:
        string name;
        string ownername;
        int subCount;
        list<string> publishedVidTitles;
    
    public:
        
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

        string GetName() const //Getter Method: uses a const state, returns a value but no parameters
        {
            return name;
        }

        void SetName(const string& newName) //Setter Method: passes the name by reference
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

        void PublishVideo(string title)
        {
            publishedVidTitles.push_back(title);
        }
};

int main()
{
    string name, title;
    string ownername; // Define the variable "ownername"
    cout << "What is the name of this channel? ";
    getline(cin, name);
    cout << "Who owns " << name << "? ";
    cin.ignore();
    getline(cin, ownername);
    YoutubeChannel ytube(name, ownername); // Object definition
    cout << "Name of the first video? ";
    cin.ignore();
    getline(cin, title);
    ytube.PublishVideo(title);
    cout << "Name of the second video? ";
    cin.ignore();
    getline(cin, title);
    ytube.PublishVideo(title);
    ytube.GetInfo(); // Call for the Class Method "GetInfo()"
    
    cout <<"This is channel 2: " << endl;
    cout << "What is the name of this channel? ";
    cin.ignore();
    getline(cin, name); //allows for string input that includes spaces
    cout << "Who owns " << name << "? ";
    cin.ignore();
    getline(cin, ownername);
    YoutubeChannel ytube2(name, ownername);
    cout << "Name of the first video? ";
    cin.ignore();
    getline(cin, title);
    ytube2.PublishVideo(title);
    cout << "Name of the second video? ";
    cin.ignore();
    getline(cin, title);
    ytube2.PublishVideo(title);
    ytube2.GetInfo();

    
}