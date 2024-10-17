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

    vector<int> idx_list(containers.size());
    iota(idx_list.begin(), idx_list.end(), 0);

    vector<vector<int>> pset;
    pset.push_back(vector<int>());

    for (auto e : idx_list)
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
    int sum = 0;
    for (auto set : pset)
    {
        for (auto e : set)
        {
            sum += containers[e];
        }
        if (sum == goal)
        {
            useful_combinations++;
        }
        sum = 0;
    }

    cout << "Part 1:" << endl
         << useful_combinations << endl;

    return 0;
}