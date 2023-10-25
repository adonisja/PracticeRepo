#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
#include <list>
using namespace std;

/* Inheritance Cont'd */

class YoutubeChannel //Class
{
    private:
        string name;
        string ownername;
        list<string>PublishedVidTitles;
        int subCount;

    public:
        YoutubeChannel(string Name, string Ownername)  //Constructor
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

        void PublishVideo(string title)
        {
            PublishedVidTitles.push_back(title);
        }

        string GetName() const
        {
            return name;
        }

        void SetName(const string& newName)
        {
            name = newName;
        }

        string GetOwner() const
        {
            return ownername;
        }

        void SetOwner(const string& newOwner)
        {
            ownername = newOwner;
        }

        void GetInfo()
        {
            cout << "Channel Name: " << name << endl;
            cout << "Owned by: " << ownername << endl;
            cout << "Videos are: " << endl;
            for (string VideoTitle : PublishedVidTitles)
            {
                cout << VideoTitle << endl; 
            }
        }
};

class CookingYoutubeChannel /* derived class */ : public YoutubeChannel  /* base class */
/* public access modifier indicates that all public methods and fields of the "YoutubeChannel" class
are inherited and made public for this derived class
*/
{
    public:
        CookingYoutubeChannel(string name, string ownername) : YoutubeChannel(name, ownername) {}
        //Constructor: <derived class>class(parameter1, parameter2) :<is passed to> base class(parameter1, parameter2) 
        
        void Practice()
        {
            cout << "This is a newbie cooking channel." << endl;
            cout << "Yea, I'm just learning and trying shyt" << endl << endl;
        }
        
};

int main()
{
    string title;
    int count;
    CookingYoutubeChannel ytChannel("Adon's World", "Akkeem"); //Object 
    ytChannel.Practice();
    cout << "How many Videos are you adding?: ";
    cin >> count;
    cin.ignore(); // ignore the newline character left in the input stream
    for (int i = 0; i < count; i++)
    {
        cout << "What is the name of this video? ";
        getline(cin, title);
        ytChannel.PublishVideo(title);
    }
    ytChannel.GetInfo();
    return 0;
}