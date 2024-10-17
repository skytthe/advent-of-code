#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main()
{
    ifstream file("2015/inputs/day17.txt");
    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    vector<int> containers;
    string line;
    while (getline(file, line))
    {
        containers.push_back(stoi(line));
    }

    vector<vector<int>> pset;
    pset.push_back(vector<int>());

    for (auto e : containers)
    {
        vector<vector<int>> new_subsets;
        for (auto set : pset)
        {
            vector<int> tmp;
            tmp = set;
            tmp.push_back(e);
            new_subsets.push_back(tmp);
        }
        pset.insert(pset.end(), new_subsets.begin(), new_subsets.end());
    }

    const int goal = 150;
    int useful_combinations = 0;
    vector<int> useful_combinations_sizes;
    int sum = 0;
    for (auto set : pset)
    {
        for (auto e : set)
        {
            sum += e;
        }
        if (sum == goal)
        {
            useful_combinations++;
            useful_combinations_sizes.push_back(set.size());
        }
        sum = 0;
    }

    sort(useful_combinations_sizes.begin(), useful_combinations_sizes.end());
    int different_ways = count(useful_combinations_sizes.begin(), useful_combinations_sizes.end(), useful_combinations_sizes[0]);

    cout << "Part 1:" << endl
         << useful_combinations << endl;

    cout << "Part 2:" << endl
         << different_ways << endl;

    return 0;
}