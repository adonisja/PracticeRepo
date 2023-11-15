#include <iostream>
#include <array>

//unsigned int oddNotPrime(unsigned int n)
void oddNotPrime()
{
  int x, i = 0;
  std::cout << "Enter a number: ";
  std::cin >> x;
  int *oddNum[] = new int [];
  int *primeNum[] = new int [];
  for (int count = 1; count <= x; count += 2)
  {
    if (count % 2 == 1)
    {
      oddNum[i] = count;
      for (int a = 2; a < count; a++)
      {
        if ((count % a) == 0)
        {
            primeNum[i] = count;
        }      
      }
    }
   i  += 1;
  }
  std::cout << "Odd Numbers: {";
  for (int count = 0; count < sizeof(oddNum); count++)
  {
    std::cout << oddNum[count] << ", ";
  }
  std::cout << "}";
  std::cout << "Prime Numbers: {";
  for (int count = 0; count < sizeof(primeNum); count++)
  {
    std::cout << oddNum[count] << ", ";
  }
  std::cout << "}";
}

int main()
{
  oddNotPrime();
  return 0;
}