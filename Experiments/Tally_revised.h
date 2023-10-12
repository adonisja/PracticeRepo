#ifndef TALLY_H
#define TALLY_H

#include "Comparable.h"

template <typename T>
class Tally : public Comparable<T> {
public:
    // Constructor
    Tally();

    // Copy constructor
    Tally(const Tally<T>& other);

    // Overloaded assignment operator
    Tally<T>& operator=(const Tally<T>& other);

    // Destructor
    ~Tally();

    // Public member functions
    void Pair(Tally<T>* ptr);
    void Add();
    const T& GetId() const;
    void SetId(const T& id);
    long Count() const;
    long Votes() const;
    void Clear();
    double GetValue() const override;
    std::string ToString() const;

private:
    // Private member variables
    T id;
    long count;
    long votes;
    Tally<T>* participants[10];
    int size;
};

#include "Tally.cpp"

#endif // TALLY_H