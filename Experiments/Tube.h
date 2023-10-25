#ifndef TUBE_H
#define TUBE_H

#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
#include <cmath>
#include <vector>
#include "../Objects/Object.h"
using namespace std;

class Tube : public Object
{
    private:
        vector<char> m_tube;
        vector<vector<char>> m_backups;
        vector<char> m_copy;
        

    public:
        Tube() : m_tube(0), m_backups(0), m_copy(0) {};

        Tube(const Tube& other) : m_tube(other.m_tube), m_backups(other.m_backups), m_copy(other.m_copy) {};

        Tube& operator=(const Tube& other)
        {
            if (this != &other)
            {
                m_tube = other.m_tube;
                m_backups = other.m_backups;
                m_copy = other.m_copy;
            }
            return *this;
        }

        ~Tube() {}

        bool Insert(char c)
        {
            if (isupper(c) && !isFull())
            {
                m_tube.push_back(c);
                return true;
            }
            else
            {
                return false;
            }
        }
        char Remove()
        {
            if (!isEmpty())
            {
                char c = m_tube.back();
                m_tube.pop_back();
                return c;
            }
            else
            {
                return '\0';
            }
        }
        char Top() const
        {
            if (!m_tube.empty())
            {
                return m_tube.back();
            }
            else
            { 
                return '\0';
            }
        }
        bool isEmpty() const
        {
            return m_tube.empty();
        }
        bool isFull() const
        {
            return m_tube.size() == 4;
        }
        bool IsOrdered() const
        {
            if (m_tube.empty())
            {
                return false;
            }
            char c = m_tube[0];
            for (int i = 1; i < m_tube.size(); i++)
            {
                if (m_tube[i] != c)
                {
                    return false;
                }
            }
            return true;
        }
        void Save()
        {
            m_backups.push_back(m_tube);
        }
        void Undo()
        {
            if (!m_backups.empty())
            {
                m_tube = m_backups.back();
                m_backups.pop_back();
            }
        }
        void Copy()
        {
            m_copy = m_tube;
        }
        void Paste()
        {
            if (!m_copy.empty())
            {
                m_tube = m_copy;
            }
        }
        void Clear()
        {
            m_tube.clear();
            m_backups.clear();
            m_copy.clear();
        }

        std::string ToString() const override {
        std::string result = "";
        for (int i = 3; i >= 0; i--) {
            if (i < m_tube.size()) {
                result += "|(";
                result += m_tube[i];
                result += ")|";
            } else {
                result += "| |";
            }
            for (int j = 0; j < 5; j++) {
                if (i == 0) {
                    result += "-";
                } else {
                    result += " ";
                }
            }
        }
        result += "\n";
        return result;
    }
};

#endif 