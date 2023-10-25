#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include "Rectangle.h"

/* void main()
{
    double length, width;
    std::cout << "What is the length: ";
    std::cin >> length;
    std::cout << "What is the width: ";
    std::cin >> width;
    Rectangle rect(length, width);
    rect.SetLength(length*8);
    rect.SetWidth(width+7);
    std::cout << "Length: " << rect.GetLength();
    std::cout << "\nWidth: " << rect.GetWidth();
    std::cout << "\nPerimeter: " << rect.Perimeter();
    std::cout << "\nArea: " << rect.Area() << "\n";
    return 0;
} */

int main()
{
    Rectangle r[6] = {Rectangle(),Rectangle(2,2),r[1],Rectangle(10,18)};
    r[4].SetLength(r[1].GetLength() * 8);
    r[4].SetWidth(r[0].GetWidth() + r[1].GetWidth());
    r[5] = r[0];

    for(int i = 0;i < 6;i += 1)
    {
        std::cout << i;
        std::cout << r[i] << "\nPerimeter: " << r[i].Perimeter();
        std::cout << "\nArea: " << r[i].Area();
        std::cout << "\n\n";
    }
    return 0;
}