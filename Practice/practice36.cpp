#include <iostream>
using namespace std;

int getMin(int num[], int size)
{
    int min = num[0];
    for (int i = 1; i < size; i += 1)
    {
        if (num[i] < min)
        {
            min = num[i];
        }
    }
    return min;
}

int getMax(int num[], int size)
{
    int max = num[0];
    for (int i = 1; i < size; i += 1)
    {
        if (num[i] > max)
        {
            max = num[i];
        }
    }
    return max;
}

void getMinAndMax(int num[], int size, int *min, int *max)
{
    for (int i = 1; i < size; i += 1)
    {
        if (num[i] < *min)
        {
            *min = num[i];
        }
        if (num[i] > *max)
        {
            *max = num[i];
        }
    }
}

int main()
{
    int num[5] = {5,4,-2,29,6};
    int min = num[0];
    int max = num[0];
    /* cout << "Min is: " << getMin(num, 5) << "\n";
    cout << "Max is: " << getMax(num, 5) << "\n";*/
    getMinAndMax(num, 5, &min, &max);
    cout << "Min is: " << min << endl;
    cout << "Max is: "<< max << endl;
    return 0;
}