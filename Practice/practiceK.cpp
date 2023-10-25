#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
#include <list>
using namespace std;

/* Constructors and Class Methods
    Rules:
        - Constructors must have the same name as your class
        - Constructors do not have a return type
*/

class YouTubeChannel //class definition: A user-defined datatype (other e.g.: char, string, etc)
{
    public: //Access modifier, class attributes are private by default, which would prevent them from being accessed in the object definition
    //properties of the class
    string name; 
    string ownername;
    int subCount;
    list <string> publishedVidTitles;

    YouTubeChannel(string name, string ownername)   //Constructor : same name as your class, and no return datatype
    {
        name = name;
        ownername = ownername;
        subCount = 0;

    }
}; //semi-colon must follow the closing curly brace in a class definition


int main()
{
    char ans;
    string vidname, name, ownername;
    list<string> videos;
    list<YouTubeChannel> channels; // create a list to store the channels
    do{
        cout << "Enter the name of your Youtube Channel: ";
        cin >> name;
        cout << endl << "Who is the owner of " << name << "?: ";
        cin >> ownername;
        YouTubeChannel ytube(name, ownername); // create a new channel object
        channels.push_back(ytube); // add the new channel to the list
        cout << "What are the videos owned by this account?: " << endl;
        cin >> 
        cout << "Do you want to create another channel? Y/N: ";
        cin >> ans;
    } while (ans != 'N');
    
    /* YouTubeChannel ytube("Adon's World", "Akkeem"); //Remember: This is the object definition used to call the class and constructor
    YouTubeChannel ytube2("Adon's Paradise", "Akkeem");
    YouTubeChannel ytube3("Adon's Dilemma", "Akkeem");
    cout << "Name: " << ytube.name << endl;
    cout << "Owner's Name: " << ytube.ownername << endl;
    cout << "Subscriber Count: " << ytube.subCount << endl;
    cout << "Videos: " << endl; */
    /* This for loop assigns each member in the list "ytube.publishedVidTitles" to a new string class
        "videoTitle" then executes the code within the loop which is outputing this new class
    */
    for (string videoTitle : ytube.publishedVidTitles)
    {
        cout << videoTitle << endl;
    }
    return 0;
}
