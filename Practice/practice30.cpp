#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
#include <list>
using namespace std;

/* Polymorphism: The ability of an Object to have multiple forms
                This means having 2 or more objects that inherit from the same base class,
                they can have a method that have the same name but different implementations
 */

class YoutubeChannel //Class
{
    private:
        string name;
        list<string>PublishedVidTitles;
        int subCount;
    
    protected:
        string ownername;
        int contentQuality;

    public:
        YoutubeChannel(string Name, string Ownername)  //Constructor
        {
            name = Name;
            ownername = Ownername;
            subCount = 0;
            contentQuality = 0;
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

        void CheckAnalytics()
        {
            if (contentQuality < 5)
            {
                cout << name << " has a 1star rating" << endl;
            }
            else if (contentQuality >= 5 && contentQuality < 9)
            {
                cout << name << " has a 2star rating" << endl;
            }
            else if (contentQuality >=9 and contentQuality < 19)
            {
                cout << name << " has a 3star rating" << endl;
            }
            else if (contentQuality >=20 and contentQuality < 50)
            {
                cout << name << " has a 4star rating" << endl;
            }
            else
            {
                cout << name << " has a 5star rating" << endl;
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
            cout << "\n" << ownername << " is a practicing a new recipe." << endl;
            contentQuality++;
        }
        
};

class SingersYoutubeChannel : public YoutubeChannel
{
    public:
        SingersYoutubeChannel(string name, string ownername) : YoutubeChannel(name, ownername) {} //Constructor
        
        void Practice()
        {
            cout << "\n" << ownername << " is practicing a new song and dance routine" << endl;
            contentQuality++;
        }
};

int main()
{
    string title;
    int count;
    CookingYoutubeChannel cookingChannel("Adon's World", "Akkeem"); //Object
    CookingYoutubeChannel* yt1 = &cookingChannel; 
    cout << "How many Videos are you adding?: ";
    cin >> count;
    cin.ignore(); // ignore the newline character left in the input stream
    for (int i = 0; i < count; i++)
    {
        cookingChannel.Practice();
        cout << "What is the name of this video? ";
        getline(cin, title);
        cookingChannel.PublishVideo(title); 
    }
    yt1->CheckAnalytics();
    cookingChannel.GetInfo();

    
    

    SingersYoutubeChannel singingChannel("Singing Sensations", "Samantha");
    SingersYoutubeChannel* yt2 = &singingChannel;
    
    cout << "How many Videos are you adding?: ";
    cin >> count;
    cin.ignore(); // ignore the newline character left in the input stream
    for (int i = 0; i < count; i++)
    {
        singingChannel.Practice();
        cout << "What is the name of this video? ";
        getline(cin, title);
        singingChannel.PublishVideo(title);
    }
    singingChannel.GetInfo();
    yt2->CheckAnalytics();
    return 0;
}