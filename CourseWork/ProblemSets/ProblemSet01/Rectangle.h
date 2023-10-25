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
        Rectangle() : length(1), width(1){} //public default constructor with default value of 1 for length and width
        
        Rectangle(double length, double width) : Rectangle() //Overloaded Constructor
        {
            if (length >= 0 && width >= 0)
            {
                if (length >= width)
                {
                    this->length = length;
                    this->width = width;
                }
                else
                {
                    this->length = width;
                    this->width = length;
                }
            }

        }

        Rectangle(const Rectangle& other) : length(other.length), width(other.width) {} //Copy Constructor

        Rectangle& operator=(const Rectangle& rhs) //Overloaded assignment operator
        {
            if (this != &rhs)
            {
                length = rhs.length;
                width = rhs.width;
            }
            return *this;
        }

        ~Rectangle() {} //Default Destructor

        double GetLength() const
        {
            return length;
        }

        double GetWidth() const
        {
            return width;
        }

        void SetLength(double newLength)
        {
            if (newLength >= 0 && newLength >= width)
            {
                length = newLength;
            }
        }

        void SetWidth(double newWidth)
        {
            if (newWidth >= 0 && newWidth <= length)
            {
                width = newWidth;
            }
        }

        double Perimeter() const
        {
            return 2*(length+width); 
        }

        double Area()
        {
            return length*width;
        }

        std::string ToString() const
        {
            std::stringstream out;

            out << std::fixed << std::setprecision(1);
            out << "[" << length << "," << width << "]";
            return out.str();
        }

        friend std::ostream& operator<<(std::ostream& out,const Rectangle& obj)
        {
            out << obj.ToString();
            return out;
        }
};

#endif