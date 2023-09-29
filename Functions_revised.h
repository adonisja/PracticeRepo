#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <fstream>
#include <string>
#include "Tally.h"

std::string Under500PrimeContent(std::ifstream& file) {
    // Create an array of Tally objects for prime factors and other prime numbers
    Tally<int> prime_factors[8];
    Tally<int> other_primes;

    // Pair the Tally objects with their respective prime factors
    prime_factors[0].Pair(new Tally<int>(2));
    prime_factors[1].Pair(new Tally<int>(3));
    prime_factors[2].Pair(new Tally<int>(5));
    prime_factors[3].Pair(new Tally<int>(7));
    prime_factors[4].Pair(new Tally<int>(11));
    prime_factors[5].Pair(new Tally<int>(13));
    prime_factors[6].Pair(new Tally<int>(17));
    prime_factors[7].Pair(new Tally<int>(19));

    // Read the numbers from the file and tally up the prime factors and other prime numbers
    int num;
    while (file >> num) {
        if (num > 0 && num <= 500) {
            bool is_prime = true;
            for (int i = 2; i < num; i++) {
                if (num % i == 0) {
                    is_prime = false;
                    prime_factors[i-2].Add();
                    break;
                }
            }
            if (is_prime) {
                other_primes.Add();
            }
        }
    }

    // Determine which tally is greatest and return the corresponding string
    int max_index = 0;
    for (int i = 1; i < 8; i++) {
        if (prime_factors[i].Count() > prime_factors[max_index].Count()) {
            max_index = i;
        }
    }
    if (prime_factors[max_index].Count() > other_primes.Count()) {
        return std::to_string(prime_factors[max_index].GetId());
    } else {
        return "others";
    }
}

#endif // FUNCTIONS_H