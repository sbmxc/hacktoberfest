// what is counting sort ?
// Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then do some arithmetic to calculate the position of each object in the output sequence. 

#include <bits/stdc++.h>
using namespace std;

// counting sort with negative values
void countSort(vector<int> &arr)
{
    // size of the array
    int size = arr.size();

    // finding the range in which value of array element lie, using STL functions
    int max = *max_element(arr.begin(), arr.end());
    int min = *min_element(arr.begin(), arr.end());
    int range = max - min + 1;

    // vector to store the frequency of each element in range
    vector<int> countStore(range);

    // iterating through the array and storing the frequency
    for (int i = 0; i < size; i++)
    {
        countStore[arr[i] - min]++;
    }

    // index will keep track of the current position in the array
    int index = 0;

    // for loop to generate the sorted array
    for (int i = 0; i < range; i++)
    {
        while (countStore[i]--)
        {
            arr[index] = i + min;
            // min must be added back
            index++;
        }
    }
}

void countSortMap(vector<int> &arr)
{
    // map to store the frequency
    map<int, int> mp;

    int size = arr.size();

    // for loop to store frequency of array elements in map
    for (int i = 0; i < size; i++)
    {
        mp[arr[i]]++;
    }

    // index keep track of the current position in the array
    int index = 0;

    // for loop to make the array sorted
    for (auto i = mp.begin(); i != mp.end(); i++)
    {
        while (i->second)
        {
            arr[index] = i->first;
            index++;
            i->second = i->second - 1;
        }
    }
}

void printArray(vector<int> &arr)
{
    for (int i : arr)
        cout << i << " ";
    cout << "\n";
}

int main()
{
    vector<int> arr = {-5, -10, 0, -3, 8, 5, -1, 10};
    countSort(arr);
    printArray(arr);
    countSortMap(arr);
    printArray(arr);
}

// Complexity analysis
// 1) vector implementation
// size of the countstore depends on the range in which values of array lie. it is possible that many numbers in the range are not present in the array but eventually space complexity and time complexity increases because of them. 
// T = O(max - min + n)
// S = O(max - min)

// 2) map implementation
// ordered map is implemented as binary search tree(BST) in c++ STL, so for insertion of an element in map it requires log(n) time, for n elements n*log(n) will be the time complexity for insertion and O(n) will be the time complexity for creating sorted array from map.
// T = O(n*logn)
// S = O(n)

//! map implementation is better when there are few elements in big range
