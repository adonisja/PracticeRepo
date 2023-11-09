#ifndef RECTANGLE_H
#define RECTANGLE_H

#include <iostream>
#include <iomanip>
#include <string>
#include <sstream> 


class Rectangle
{
    private:
        double length;
        double width;

    public:
        Rectangle () : length(1), width(1) {}   //Constructor
        Rectangle(const Rectangle &obj)         //Copy Constructor
        {
            length = obj.length;
            width = obj.width;
        }

        Rectangle& operator=(const Rectangle &rhs) //Assignment operator
        {
            if (this != &rhs)
            {
                length = rhs.length;
                width = rhs.width;
            }
            return *this;
        }
        ~Rectangle() {}     //Destructor

        double GetLength()
        {
            return length;
        }

        double GetWidth()
        {
            return width;
        }

        void SetLength(double value)
        {
            if (value > 0 && value >= width)
            {
                length = value;
            }
        }

        void SetWidth(double value)
        {
            if (value > 0 && value <= length)
            {
                width = value;
            }
        }

        double Perimeter() const
        {
            return 2*(length+width);
        }

        double Area() const
        {
            return length*width;
        }

        std::string ToString() const
        {
            std::stringstream out;
            out << std::fixed << std::setprecision(1);
            out << "[" << length << ", " << width << "]\n";
            return out.str();
        }

        friend std::ostream& operator<<(std::ostream& out, const Rectangle& obj)
        {
            out << obj.ToString();
            return out;
        }
};

#endif
