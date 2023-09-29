#ifndef EXTRA_H
#define EXTRA_H

#include <iostream>
#include <string>

class LetterSet {
public:
    // Constructor
    LetterSet();

    // Copy constructor
    LetterSet(const LetterSet& other);

    // Overloaded assignment operator
    LetterSet& operator=(const LetterSet& other);

    // Destructor
    ~LetterSet();

    // Public member functions
    bool Insert(char c);
    bool Remove(char c);
    bool Contains(char c) const;
    bool IsEmpty() const;
    bool IsFull() const;
    long Count() const;
    void Clear();
    std::string ToString() const;

    // Friend function
    friend std::ostream& operator<<(std::ostream& os, const LetterSet& ls);

private:
    // Private member variables
    bool data[26];
};

#endif // EXTRA_H