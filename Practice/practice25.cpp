#include <iostream>
#include <climits>
#include <iomanip>
#include <cmath>
#include <list>
using namespace std;

/*  Object Oriented Programming
Class: A template or blueprint (e.g.: a fruit) , a class is a user defined datatype
Object: An example of a class (e.g.: a banana, an apple)
*/

class YouTubeChannel //class definition
{
    public: //Access modifier, class attributes are private by default, which would prevent them from being accessed in the object definition
    //properties of the class
    string name; 
    string ownername;
    int subCount;
    list <string> publishedVidTitles;
}; //semi-colon must follow the closing curly brace in a class definition

int main()
{
    YouTubeChannel ytube; //Object definition
    ytube.name = "Adon's World";
    ytube.ownername = "Akkeem";
    ytube.subCount = 1800;
    ytube.publishedVidTitles = {"C++ for Beginners Video 1", "HTML & CSS Video 1", "C++ OOP Video 1"} ;
    cout << "Name: " << ytube.name << endl;
    cout << "Owner's Name: " << ytube.ownername << endl;
    cout << "Subscriber Count: " << ytube.subCount << endl;
    cout << "Videos: " << endl;
    /* This for loop assigns each member in the list "ytube.publishedVidTitles" to a new string class
        "videoTitle" then executes the code within the loop which is outputing this new class
    */
    for (string videoTitle : ytube.publishedVidTitles) // for the list of videos in my youtube channel list, print out, each video title
    {
        cout << videoTitle << endl;
    }
    return 0;
}
