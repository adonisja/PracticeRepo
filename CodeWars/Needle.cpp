#include <vector>
#include <string>
#include <iostream>

std::string findNeedle(const std::vector<std::string>& haystack)
{
    std::vector<std::string> wordArray;
    std::cout << "Enter a set of words or press 999 to exit: ";
    std::string word;
    while (std::cin >> word && word != "999")
    {
        wordArray.push_back(word);
    }
    for (int i = 0; i < wordArray.size(); i++)
    {
        if (wordArray[i] == "needle")
        {
            return "found the needle at position " + std::to_string(i + 1);
        }
    }
    return "needle not found";
}