#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        vector<int> ret;        //Declares a vector of integers
        int size = nums.size(); 
        int diff = 0;
        unordered_map<int, int>map;     
        /*declares an unordered map type named map to store an int key and an int value pair 
            This map is initially empty */
        for(int i = 0; i < size; i++)
        {
            diff = target - nums[i];
            if (map.find(diff) != map.end() && map.find(diff)->second != i)
            /* This checks if the diff is a key in the map (it checks if diff is contained in any value in the map)
                So map.find(diff) != map.end() is true if diff is a key in the map 
                
                map.find(diff)->second != i: If diff is a key in map, this checks if the value associated with diff(index) is not
                the same as the current index 'i'. The ->second operator is used to access the value associated with the key
                in an unordered map*/
            {
                ret.push_back(i); //adds the index of i to the vector
                ret.push_back(map.find(diff)->second); //adds the index of difference to the vector if the conditions above are true
                return ret;
            }
            else
            {
                map[nums[i]] = i; //adds the value of i and its index to the map
            }
        }
        return ret;
    }
};