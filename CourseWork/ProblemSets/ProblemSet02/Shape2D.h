#ifndef SHAPE_2D.H
#define SHAPE_2D.H

#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>

class Shape2D  
{  
    public:
        virtual double Area() const = 0; // A pure double constant virtual method
};
    
class Circle : public Shape2D
{
    private:
        double radius;

    public:
        Circle() : radius (1) {}

        Circle(const Circle& other) : radius(other.radius) {}  

        Circle& operator=(const Circle& rhs)
        {
            if (this != &rhs)
            {
                radius = rhs.radius;
            }
            return *this;
        }

        ~Circle() {}

        double GetRadius() const
        {
            return radius;
        }

        void SetRadius(double value)
        {
            if (value >= 0)
            {
                radius = value;
            }
        }

        double Circumference() const
        {
            return 6.28318 * radius;
        }

        double Area() const override
        {
            return 3.14159 * radius * radius;
        }

        std::string ToString() const
        {
            std::stringstream out;

            out << std::fixed << std::setprecision(2);
            out << "((" << radius << "))";
            return out.str();
        }

        friend std::ostream& operator<<(std::ostream& out, const Circle& obj)
        {
            out << obj.ToString();
            return out;
        }
};

class RegularPolygon : public Shape2D
{
    private: 
        double sides;
        int count;

    public:
        RegularPolygon() : sides(1), count(3) {}

        RegularPolygon(RegularPolygon& other) : sides(other.sides), count(other.count) {}

        RegularPolygon& operator=(const RegularPolygon& rhs)
        {
            if (this != &rhs)
            {
                sides = rhs.sides;
                count = rhs.count;
            }
            return *this;
        }

        ~RegularPolygon() {}

        double GetSides() const
        {
            return sides;
        }

        int GetCount() const
        {
            return count;
        }

        void SetSides(double value)
        {
            if (value >= 1)
            sides = value;
        }

        void SetCount(int value)
        {
            if (value >= 1)
            {
                count = value;
            }
        }

        double Perimeter()
        {
            return sides*count;
        }

        std::string ToString() const
        {
            std::stringstream out;

            std::fixed
        }

        })
};




#endif