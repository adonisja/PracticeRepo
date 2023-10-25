#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
#include <list>
using namespace std;

class YoutubeChannel //class definition
{
    public:
        string name;
        string ownername;
        int subCount;
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
    void GetInfo() //Class Method: defines the behaviour of a class
    {   
    
    cout << "Channel Name: " << name << endl;
    cout << "Owned by: " << ownername << endl;
    cout << "Videos are: " << endl;
    for (string VideoTitle : publishedVidTitles)
    {
        cout << VideoTitle << endl; 
    }
    cout << "Subscriber Count: " << subCount << endl << endl;
    }
};

int main()
{
    YoutubeChannel ytube("Adon's World", "Akkeem"); // Object definition
    ytube.publishedVidTitles.push_back("C++ for Beginners"); //push_back adds an element at the end of the "publishedVidTitles" list
    ytube.publishedVidTitles.push_back("Coding Practice 101");
    ytube.GetInfo(); // Call for the Class Method "GetInfo()"
    YoutubeChannel ytube2("Adon's Paradise", "Akkeem");
    ytube2.publishedVidTitles.push_back("Biology 101");
    ytube2.publishedVidTitles.push_back("Biology for Dummies");
    ytube2.GetInfo();
    
}